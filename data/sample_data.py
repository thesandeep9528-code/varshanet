import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Tuple

from data.districts import get_all_districts, INDIAN_STATES, DISTRICT_COORDS
from models.regime_classifier import RegimeClassifier
from models.bias_correction import BiasCorrector

class SampleDataGenerator:
    """
    Generates realistic synthetic monsoon data.
    """
    
    def __init__(self):
        self.regimes = RegimeClassifier.REGIMES
        self.bias_corrector = BiasCorrector()
        
    def _generate_synthetic_rainfall(self, size: int, regime: str) -> np.ndarray:
        """Generates raw forecast and observed rainfall using Gamma distributions."""
        if regime == "Active Monsoon":
            raw_fcst = np.random.gamma(shape=2.0, scale=15.0, size=size)
            obs = raw_fcst * np.random.uniform(0.8, 1.5, size)
        elif regime == "Break Monsoon":
            raw_fcst = np.random.gamma(shape=1.0, scale=5.0, size=size)
            obs = raw_fcst * np.random.uniform(0.3, 0.9, size)
            obs[obs < 2.0] = 0.0 # Make dry days truly dry
        elif regime == "Monsoon Depression/Low":
            raw_fcst = np.random.gamma(shape=3.0, scale=25.0, size=size)
            obs = raw_fcst * np.random.uniform(1.2, 2.0, size) # Underprediction typical
        else:
            raw_fcst = np.random.gamma(shape=1.5, scale=10.0, size=size)
            obs = raw_fcst * np.random.uniform(0.7, 1.3, size)
            
        # Ensure non-negative
        raw_fcst = np.maximum(0, raw_fcst)
        obs = np.maximum(0, obs)
        return raw_fcst, obs

    def generate_forecast_data(self, date: str, n_districts: int = 50) -> pd.DataFrame:
        """Generates tabular forecast data for multiple districts on a specific date."""
        all_districts = get_all_districts()
        selected = np.random.choice(all_districts, n_districts, replace=False)
        
        data = []
        for dist in selected:
            # Find state
            state = next(s for s, d_list in INDIAN_STATES.items() if dist in d_list)
            lat, lon = DISTRICT_COORDS.get(dist, (20.0, 78.0))
            
            # Assign random regime for this day based loosely on location
            regime = np.random.choice(self.regimes)
            if lat > 25 and np.random.rand() < 0.3:
                regime = "Western Disturbance"
            
            raw, obs = self._generate_synthetic_rainfall(1, regime)
            raw = float(raw[0])
            obs = float(obs[0])
            
            corrected = self.bias_corrector.correct(raw, regime, {"elevation": 500, "wind_dir": 270})
            prob = self.bias_corrector.compute_heavy_rainfall_probability(corrected)
            
            data.append({
                "date": date,
                "district": dist,
                "state": state,
                "lat": lat,
                "lon": lon,
                "raw_forecast": round(raw, 1),
                "regime": regime,
                "corrected_forecast": corrected,
                "observed": round(obs, 1),
                "heavy_rain_prob": prob
            })
            
        return pd.DataFrame(data)
        
    def generate_regime_map_data(self) -> pd.DataFrame:
        """Generates regime classification for a grid over India."""
        lats = np.arange(6, 39, 1.0)
        lons = np.arange(68, 99, 1.0)
        
        data = []
        # Simulate a cohesive regime pattern (e.g., active trough)
        for lat in lats:
            for lon in lons:
                if 18 <= lat <= 25 and 75 <= lon <= 85:
                    reg = "Active Monsoon"
                elif lat > 28 and lon < 78:
                    reg = "Western Disturbance"
                elif 8 <= lat <= 15 and 73 <= lon <= 77:
                    reg = "Orographic Rainfall"
                else:
                    reg = "Break Monsoon"
                    
                data.append({"lat": lat, "lon": lon, "regime": reg})
                
        return pd.DataFrame(data)

    def generate_time_series(self, district: str, days: int = 30) -> pd.DataFrame:
        """Generates daily time series data for a district."""
        base_date = datetime.now() - timedelta(days=days)
        data = []
        
        # Keep regime persistent for a few days
        current_regime = np.random.choice(self.regimes)
        regime_duration = np.random.randint(3, 8)
        
        for i in range(days):
            date_str = (base_date + timedelta(days=i)).strftime("%Y-%m-%d")
            
            if regime_duration == 0:
                current_regime = np.random.choice(self.regimes)
                regime_duration = np.random.randint(3, 8)
            regime_duration -= 1
            
            raw, obs = self._generate_synthetic_rainfall(1, current_regime)
            raw = float(raw[0])
            obs = float(obs[0])
            
            corrected = self.bias_corrector.correct(raw, current_regime)
            
            data.append({
                "date": date_str,
                "district": district,
                "raw_forecast": round(raw, 1),
                "corrected_forecast": corrected,
                "observed": round(obs, 1),
                "regime": current_regime
            })
            
        return pd.DataFrame(data)
        
    def generate_verification_data(self, n_samples: int = 1000) -> pd.DataFrame:
        """Generates synthetic paired forecast-observation data for verification."""
        data = []
        for reg in self.regimes:
            samples_per_regime = n_samples // len(self.regimes)
            raw, obs = self._generate_synthetic_rainfall(samples_per_regime, reg)
            
            for r, o in zip(raw, obs):
                c = self.bias_corrector.correct(r, reg)
                data.append({
                    "regime": reg,
                    "raw_forecast": r,
                    "corrected_forecast": c,
                    "observed": o
                })
                
        return pd.DataFrame(data)
