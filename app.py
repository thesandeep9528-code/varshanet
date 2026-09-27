"""
VarshaNet 2.0 — Regime-Aware AI Post-Processing of Monsoon Rainfall Forecasts
Flask Application Server

Ministry of Earth Sciences (MoES)
National Centre for Medium Range Weather Forecasting (NCMRWF)
"""

from flask import Flask, render_template, request, jsonify
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

# ─── Lazy initialisation of ML models ──────────────────────────────────
_classifier = None
_corrector = None
_verifier = None
_data_gen = None


def get_classifier():
    global _classifier
    if _classifier is None:
        from models.regime_classifier import RegimeClassifier
        _classifier = RegimeClassifier()
    return _classifier


def get_corrector():
    global _corrector
    if _corrector is None:
        from models.bias_correction import BiasCorrector
        _corrector = BiasCorrector()
    return _corrector


def get_verifier():
    global _verifier
    if _verifier is None:
        from models.verification import ForecastVerifier
        _verifier = ForecastVerifier()
    return _verifier


def get_data_gen():
    global _data_gen
    if _data_gen is None:
        from data.sample_data import SampleDataGenerator
        _data_gen = SampleDataGenerator()
    return _data_gen


# ─── State list for templates ──────────────────────────────────────────
from data.districts import INDIAN_STATES, get_all_districts, DISTRICT_COORDS

STATES_LIST = sorted(INDIAN_STATES.keys())


# ─── Page routes ───────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html', date=datetime.now().strftime("%d %b %Y"))


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', date=datetime.now().strftime("%d %b %Y"))


@app.route('/regime')
def regime():
    return render_template('regime.html')


@app.route('/forecast')
def forecast():
    return render_template('forecast.html', states=STATES_LIST)


@app.route('/verification')
def verification():
    return render_template('verification.html')


@app.route('/about')
def about():
    return render_template('about.html')


# ─── API endpoints ────────────────────────────────────────────────────

@app.route('/api/classify', methods=['POST'])
def api_classify():
    """Classify the weather regime from meteorological parameters."""
    data = request.get_json(force=True) if request.is_json else request.form.to_dict()

    # Map region to approximate lat/lon for the classifier
    region_coords = {
        "Central India": (22.0, 79.0),
        "Western Coast": (14.0, 74.5),
        "Eastern Coast": (16.0, 81.0),
        "NW India": (30.0, 74.0),
        "NE India": (26.0, 92.0),
    }
    lat, lon = region_coords.get(data.get("region", "Central India"), (22.0, 79.0))

    params = {
        "mslp_anomaly": float(data.get("mslp", -2)),
        "wind_speed_850": float(data.get("wind", 15)),
        "olr_anomaly": float(data.get("olr", -20)),
        "moisture_flux": float(data.get("moisture", 200)),
        "vorticity_850": float(data.get("vorticity", 2.0)) * 1e-5,
        "lat": lat,
        "lon": lon,
    }

    classifier = get_classifier()
    result = classifier.classify(params)

    return jsonify({
        "regime": result["regime"],
        "confidence": round(result["confidence_score"] * 100, 1),
        "description": classifier.get_regime_description(result["regime"]),
        "key_indicators": result["key_indicators"],
    })


@app.route('/api/forecast-data')
def api_forecast_data():
    """Return district-level forecast data, optionally filtered by state."""
    state_filter = request.args.get('state', '')
    date_str = datetime.now().strftime("%Y-%m-%d")

    data_gen = get_data_gen()
    df = data_gen.generate_forecast_data(date_str, n_districts=100)

    if state_filter:
        df = df[df['state'] == state_filter]

    records = []
    for _, row in df.iterrows():
        prob_pct = round(row['heavy_rain_prob'] * 100, 1) if row['heavy_rain_prob'] < 1 else round(row['heavy_rain_prob'], 1)
        records.append({
            "district": row["district"],
            "state": row["state"],
            "lat": row["lat"],
            "lon": row["lon"],
            "raw": row["raw_forecast"],
            "corrected": row["corrected_forecast"],
            "regime": row["regime"],
            "prob_heavy": prob_pct,
        })

    return jsonify(records)


@app.route('/api/regime-map')
def api_regime_map():
    """Return grid-wise regime classification over India."""
    data_gen = get_data_gen()
    df = data_gen.generate_regime_map_data()
    return jsonify(df.to_dict(orient='records'))


@app.route('/api/verification-data')
def api_verification_data():
    """Return comprehensive verification metrics comparing Raw vs Corrected."""
    data_gen = get_data_gen()
    verifier = get_verifier()

    vdf = data_gen.generate_verification_data(n_samples=600)

    observed = vdf['observed'].values
    raw = vdf['raw_forecast'].values
    corrected = vdf['corrected_forecast'].values

    comparison = verifier.compare_forecasts(observed, raw, corrected)

    # Also compute regime-wise metrics
    regime_metrics = {}
    for regime_name, grp in vdf.groupby('regime'):
        o, r, c = grp['observed'].values, grp['raw_forecast'].values, grp['corrected_forecast'].values
        raw_m = verifier.verify(o, r, thresholds=[2.5, 15.6, 64.5])
        corr_m = verifier.verify(o, c, thresholds=[2.5, 15.6, 64.5])
        regime_metrics[regime_name] = {
            "raw_rmse": raw_m["continuous"]["RMSE"],
            "corrected_rmse": corr_m["continuous"]["RMSE"],
            "raw_corr": raw_m["continuous"]["Correlation"],
            "corrected_corr": corr_m["continuous"]["Correlation"],
        }

    return jsonify({
        "comparison": comparison,
        "regime_wise": regime_metrics,
    })


@app.route('/api/district-timeseries')
def api_district_timeseries():
    """Return 30-day time series for a given district."""
    district = request.args.get('district', 'Mumbai')
    data_gen = get_data_gen()
    df = data_gen.generate_time_series(district, days=30)

    return jsonify({
        "dates": df['date'].tolist(),
        "raw_forecast": df['raw_forecast'].tolist(),
        "corrected_forecast": df['corrected_forecast'].tolist(),
        "observed": df['observed'].tolist(),
        "regimes": df['regime'].tolist(),
    })


# ─── Run ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
