import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from typing import Dict, Any, Tuple, List

class RegimeClassifier:
    """
    Classifies Indian monsoon regimes based on meteorological parameters.
    """
    
    REGIMES = [
        "Active Monsoon",
        "Break Monsoon",
        "Monsoon Depression/Low",
        "Orographic Rainfall",
        "Coastal Rainfall",
        "Western Disturbance"
    ]
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False
        self.feature_names = ["mslp_anomaly", "wind_speed_850", "olr_anomaly", 
                              "moisture_flux", "vorticity_850", "lat", "lon"]
        self._train_prototype_model()
        
    def _train_prototype_model(self):
        """Trains a prototype model using synthetic but realistic data."""
        X, y = self._generate_training_data()
        self.model.fit(X, y)
        self.is_trained = True
        
    def _generate_training_data(self) -> Tuple[pd.DataFrame, np.ndarray]:
        """Generates realistic synthetic data for training."""
        np.random.seed(42)
        n_samples = 3000
        n_per_class = n_samples // len(self.REGIMES)
        
        X_data = []
        y_data = []
        
        for i, regime in enumerate(self.REGIMES):
            # Base values for lat/lon depending on region typically affected
            if regime == "Active Monsoon":
                lat = np.random.uniform(18, 25, n_per_class)
                lon = np.random.uniform(73, 85, n_per_class)
                mslp = np.random.normal(-2, 1, n_per_class)
                wind = np.random.normal(15, 3, n_per_class)
                olr = np.random.normal(-20, 10, n_per_class)
                moisture = np.random.normal(200, 30, n_per_class)
                vort = np.random.normal(1.5e-5, 0.5e-5, n_per_class)
            elif regime == "Break Monsoon":
                lat = np.random.uniform(25, 30, n_per_class) # shifted north
                lon = np.random.uniform(75, 88, n_per_class)
                mslp = np.random.normal(2, 1, n_per_class)
                wind = np.random.normal(5, 2, n_per_class)
                olr = np.random.normal(20, 10, n_per_class)
                moisture = np.random.normal(100, 30, n_per_class)
                vort = np.random.normal(0, 0.2e-5, n_per_class)
            elif regime == "Monsoon Depression/Low":
                lat = np.random.uniform(19, 23, n_per_class)
                lon = np.random.uniform(80, 88, n_per_class) # Bay of Bengal/East Coast
                mslp = np.random.normal(-5, 1.5, n_per_class)
                wind = np.random.normal(20, 5, n_per_class)
                olr = np.random.normal(-40, 15, n_per_class)
                moisture = np.random.normal(300, 50, n_per_class)
                vort = np.random.normal(4e-5, 1e-5, n_per_class)
            elif regime == "Orographic Rainfall":
                lat = np.random.uniform(10, 20, n_per_class)
                lon = np.random.uniform(73, 76, n_per_class) # Western Ghats
                mslp = np.random.normal(-1, 0.5, n_per_class)
                wind = np.random.normal(25, 5, n_per_class) # Strong westerlies
                olr = np.random.normal(-15, 8, n_per_class)
                moisture = np.random.normal(250, 40, n_per_class)
                vort = np.random.normal(1e-5, 0.5e-5, n_per_class)
            elif regime == "Coastal Rainfall":
                lat = np.random.uniform(8, 15, n_per_class)
                lon = np.random.uniform(74, 80, n_per_class) 
                mslp = np.random.normal(0, 1, n_per_class)
                wind = np.random.normal(10, 3, n_per_class)
                olr = np.random.normal(-10, 5, n_per_class)
                moisture = np.random.normal(180, 20, n_per_class)
                vort = np.random.normal(0.5e-5, 0.3e-5, n_per_class)
            elif regime == "Western Disturbance":
                lat = np.random.uniform(28, 36, n_per_class) # NW India
                lon = np.random.uniform(70, 78, n_per_class)
                mslp = np.random.normal(-1, 2, n_per_class)
                wind = np.random.normal(12, 4, n_per_class)
                olr = np.random.normal(-15, 10, n_per_class)
                moisture = np.random.normal(120, 25, n_per_class)
                vort = np.random.normal(2e-5, 0.8e-5, n_per_class)
                
            class_data = np.column_stack([mslp, wind, olr, moisture, vort, lat, lon])
            X_data.append(class_data)
            y_data.extend([i] * n_per_class)
            
        X = np.vstack(X_data)
        y = np.array(y_data)
        
        return pd.DataFrame(X, columns=self.feature_names), y

    def classify(self, parameters: Dict[str, float]) -> Dict[str, Any]:
        """
        Classifies the regime based on input parameters.
        """
        if not self.is_trained:
            raise ValueError("Model is not trained.")
            
        input_df = pd.DataFrame([parameters], columns=self.feature_names)
        
        # Predict class and probabilities
        pred_idx = self.model.predict(input_df)[0]
        probs = self.model.predict_proba(input_df)[0]
        
        regime = self.REGIMES[pred_idx]
        confidence = float(probs[pred_idx])
        
        # Determine key indicators
        indicators = []
        if parameters.get('mslp_anomaly', 0) < -3:
            indicators.append("Strong negative MSLP anomaly")
        if parameters.get('vorticity_850', 0) > 3e-5:
            indicators.append("High lower-level vorticity")
        if parameters.get('moisture_flux', 0) > 250:
            indicators.append("Strong moisture flux")
            
        return {
            "regime": regime,
            "confidence_score": confidence,
            "key_indicators": indicators
        }
        
    def get_regime_description(self, regime: str) -> str:
        """Returns description text for a given regime."""
        descriptions = {
            "Active Monsoon": "Strong monsoon trough, high moisture, widespread rainfall over central and plain regions.",
            "Break Monsoon": "Weak/shifted trough to foothills, suppressed rainfall over central India, enhanced over NE and foothills.",
            "Monsoon Depression/Low": "Organized low-pressure system, causing heavy localized rainfall, typically originating in Bay of Bengal.",
            "Orographic Rainfall": "Enhanced rainfall by topography, notably the Western Ghats or NE hills.",
            "Coastal Rainfall": "Coastal convergence events bringing significant rain to coastal stretches.",
            "Western Disturbance": "Extratropical influence bringing winter/pre-monsoon rain to NW India."
        }
        return descriptions.get(regime, "Unknown regime.")
