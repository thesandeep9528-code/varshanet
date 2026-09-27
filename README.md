# 🌧️ VarshaNet

## AI-Based Regime-Aware Post-Processing for Improved Monsoon Rainfall Forecasts

**Smart India Hackathon 2026 — Problem Statement ID: 26080**
**Problem Statement:** Regime-Aware AI Post-Processing of Monsoon Rainfall Forecasts
**Theme:** Smart Automation
**Category:** Software
**Team:** SquadY
**Team ID:** 182149

---

## 📌 Overview

**VarshaNet** is an AI/ML-based rainfall post-processing system designed to improve raw **Numerical Weather Prediction (NWP)** rainfall forecasts by considering the prevailing weather regime.

Rainfall forecast errors can vary across different meteorological situations such as **Active Monsoon, Break Monsoon, Low/Depression, Orographic, Coastal and Western Disturbance regimes**. A single static bias-correction method may therefore not perform consistently across all regimes.

VarshaNet follows a **regime-aware post-processing approach**:

```text
Raw NWP Rainfall Forecast
          ↓
Weather Regime Classification
          ↓
Regime-Specific Bias Correction
          ↓
Extreme Rainfall Modeling
          ↓
Threshold-Exceedance Probability
          ↓
District-Level Rainfall Product
          ↓
Verification
```

---

## 🎯 Problem Statement

Traditional rainfall forecasts can contain systematic errors that vary with the prevailing weather regime.

The objective of VarshaNet is to build an AI/ML-based system that:

* Identifies the prevailing weather regime.
* Applies suitable regime-specific correction to raw NWP rainfall forecasts.
* Improves rainfall forecasts at grid/district level.
* Estimates the probability of Heavy and Very Heavy Rainfall events.
* Provides a user-friendly district-level rainfall product.
* Verifies forecast skill against observed rainfall.

---

## 💡 Proposed Solution

### 1. Weather Regime Classification

The system identifies the prevailing weather regime using NWP and atmospheric/synoptic predictors.

Supported regimes include:

* Active Monsoon
* Break Monsoon
* Low / Depression
* Orographic Rainfall
* Coastal Rainfall
* Western Disturbance

### 2. Regime-Specific Bias Correction

Instead of applying one global correction method, VarshaNet uses the detected weather regime as contextual information for rainfall post-processing.

```text
Raw NWP Forecast + Detected Weather Regime
                    ↓
          Regime-Specific Correction
                    ↓
          Corrected Rainfall Forecast
```

### 3. Extreme-Rainfall Modeling

The system focuses on regime-conditioned rainfall error patterns, particularly for:

* Heavy Rainfall
* Very Heavy Rainfall
* Extreme Rainfall

### 4. Probabilistic Forecasting

VarshaNet estimates rainfall threshold-exceedance probability:

```text
P(Rainfall > Operational Threshold)
```

This provides probabilistic information for heavy-rainfall risk assessment.

### 5. District-Level Rainfall Product

Grid-level rainfall information can be transformed into:

* District-wise rainfall forecasts
* Rainfall maps
* Forecast tables
* Threshold-exceedance information

### 6. Verification

Forecast performance is evaluated against observed rainfall using:

* RMSE
* ETS
* CSI
* POD
* FAR
* FSS

---

## 🏗️ System Architecture

```text
┌───────────────────────────────┐
│       NWP Forecast Data       │
│     Rainfall + Atmosphere     │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       Data Processing         │
│ NWP + Observations + Features │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│   Weather Regime Classifier   │
│ Active | Break | Depression   │
│ Orographic | Coastal | WD     │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│ Regime-Specific Bias          │
│ Correction / Post-Processing  │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│   Extreme Rainfall Modeling   │
│ Heavy / Very Heavy / Extreme  │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│ Probabilistic Forecasting     │
│ P(Rainfall > Threshold)       │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│    District-Level Product     │
│       Map + Table + Data      │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│          Verification         │
│ RMSE | ETS | CSI | POD | FAR │
│             | FSS             │
└───────────────────────────────┘
```

---

## 📊 Data Sources

### Observed Rainfall / Ground Truth

The project uses the **IMD Gridded Rainfall Dataset** as the observed rainfall reference for verification.

* Spatial resolution: 0.25° × 0.25°
* Historical daily rainfall data over India

### Raw NWP Forecasts

The proposed system uses NWP rainfall forecasts and relevant atmospheric variables.

Examples mentioned in the project:

* GFS
* NGFS
* NEPS
* Rainfall
* Wind fields
* OLR
* Other atmospheric/synoptic predictors

### Regime Information

Weather regime identification can use:

* Circulation indices
* Monsoon indices
* OLR
* Wind fields
* Published objective regime criteria

---

## 🧠 AI/ML Pipeline

```text
Data Ingestion
      ↓
Feature Preparation
      ↓
Weather Regime Classification
      ↓
Regime-Specific Bias Correction
      ↓
Extreme Rainfall Modeling
      ↓
Probabilistic Forecasting
      ↓
District-Level Processing
      ↓
Verification
```

The project architecture is designed to condition rainfall post-processing on the prevailing meteorological regime rather than relying only on a single static correction.

---

## 📈 Verification Framework

VarshaNet is designed to compare the post-processed forecast against the **Raw NWP baseline** and observed rainfall.

### Continuous Forecast Verification

**RMSE — Root Mean Square Error**

Measures the magnitude of rainfall forecast error.

### Categorical / Event Verification

* **ETS — Equitable Threat Score**
* **CSI — Critical Success Index**
* **POD — Probability of Detection**
* **FAR — False Alarm Ratio**

These metrics can be used to evaluate Heavy and Very Heavy Rainfall events.

### Spatial Verification

**FSS — Fractions Skill Score**

Used for evaluating the spatial skill of rainfall forecasts.

---

## 🔬 Technology Stack

### Programming & AI/ML

* Python
* XGBoost / LightGBM
* Machine Learning

### Data Processing

* Pandas
* NumPy
* Xarray

### Geospatial Processing

* GeoPandas
* Rasterio
* QGIS

### Visualization

* Matplotlib
* Plotly
* Folium

### Weather & Climate Data

* NWP Forecasts
* IMD Observations
* ERA5

### Deployment / Backend

* FastAPI
* Docker
* AWS

### Database

* PostgreSQL
* PostGIS

### Dashboard

* Streamlit
* React

> Technologies listed above represent the proposed project stack; the final repository should reflect only components actually implemented in the prototype.

---

## 🌦️ Key Features

* 🤖 AI/ML-based weather regime classification
* 🌧️ Regime-specific rainfall bias correction
* ⛈️ Heavy and Very Heavy Rainfall modeling
* 📊 Threshold-exceedance probability
* 🗺️ District-level rainfall visualization
* 📍 Grid-level forecast processing
* 📈 Quantitative forecast verification
* 🔎 Comparison against Raw NWP forecasts
* 🧩 Modular post-processing architecture

---

## 🎯 Expected Outcomes

| Expected Outcome                 | VarshaNet Output                                        |
| -------------------------------- | ------------------------------------------------------- |
| Weather Regime Classifier        | Active / Break / Depression / Coastal / Orographic / WD |
| Bias-Corrected Rainfall Forecast | Regime-specific corrected rainfall                      |
| Heavy Rainfall Probability       | Threshold-exceedance probability                        |
| District-Level Rainfall Product  | Map + Table                                             |
| Verification Report              | RMSE, ETS, CSI, POD, FAR, FSS                           |

---

## 🌍 Potential Applications

### Agriculture

Improved rainfall information for crop planning, irrigation and heavy-rainfall preparedness.

### Disaster Management

Heavy and Very Heavy Rainfall probability information for risk assessment and preparedness.

### District Administration

District-level rainfall maps, tables and threshold-exceedance information for operational planning.

### Water Management

Rainfall information supporting reservoir, flood and water-resource planning.

### NWP Post-Processing

Transforms raw NWP rainfall forecasts into regime-aware, bias-corrected and probabilistic rainfall products.

---

## 🔮 Future Scope

* Improve regime classification using additional atmospheric predictors.
* Extend probabilistic post-processing and calibration.
* Incorporate additional NWP models and ensemble information.
* Improve district-level spatial processing.
* Perform extensive multi-year temporal validation.
* Extend the framework to other weather regimes and extreme-weather applications.
* Develop an operational real-time forecasting dashboard.

---

## 📂 Project Structure

```text
VarshaNet/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── observations/
│
├── models/
│   ├── regime_classifier/
│   ├── bias_correction/
│   └── rainfall_model/
│
├── preprocessing/
│
├── forecasting/
│
├── verification/
│
├── visualization/
│
├── dashboard/
│
├── api/
│
├── notebooks/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/varshanet.git
cd varshanet
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Project

Use the project-specific entry point:

```bash
python <entry_file>.py
```

or, if the dashboard is implemented using Streamlit:

```bash
streamlit run <dashboard_file>.py
```

---

## 🖥️ Prototype

### Live Prototype

**Coming Soon / Add Link**

### GitHub Repository

**This Repository**

### Demo

**Add demo video or deployment link here**

---

## 📸 Prototype Screenshots

Add screenshots of:

1. Weather Regime Classification
2. Raw NWP Rainfall Forecast
3. VarshaNet Bias-Corrected Forecast
4. Heavy Rainfall Probability
5. District-Level Rainfall Map/Table
6. Verification Results

---

## 📚 References

The project is based on research and datasets related to:

* IMD Gridded Rainfall Dataset
* Indian monsoon circulation and regime indices
* Probabilistic Quantitative Precipitation Forecasting
* Regime-dependent post-processing of NWP forecasts
* AI-enabled monsoon forecasting systems

Specific references and data sources are documented in the project presentation and repository documentation.

---

## 👥 Team

### SquadY

**Team ID:** 182149
**Smart India Hackathon 2026**
**Problem Statement ID:** 26080

---

## 🏆 Smart India Hackathon 2026

**Problem Statement:**
**Regime-Aware AI Post-Processing of Monsoon Rainfall Forecasts**

**Theme:** Smart Automation
**Category:** Software

> **VarshaNet — From Raw NWP Forecasts to Regime-Aware, Probabilistic and District-Level Rainfall Information.**
