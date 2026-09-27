import numpy as np
import scipy.stats as stats
from typing import Dict, Any, Union

class BiasCorrector:
    """
    Applies regime-aware bias correction to raw rainfall forecasts.
    """
    
    IMD_THRESHOLDS = {
        "Light": (2.5, 15.5),
        "Moderate": (15.6, 64.4),
        "Heavy": (64.5, 115.5),
        "Very Heavy": (115.6, 204.4),
        "Extremely Heavy": (204.5, float('inf'))
    }
    
    def __init__(self):
        pass
        
    def correct(self, raw_forecast: float, regime: str, additional_params: Dict[str, Any] = None) -> float:
        """
        Corrects a raw rainfall forecast based on its regime.
        """
        if additional_params is None:
            additional_params = {}
            
        # Base correction factor
        corrected = raw_forecast
        
        if regime == "Active Monsoon":
            # Quantile mapping with wet-day adjustment (simplified heuristic)
            if raw_forecast > 2.5:
                # Enhance moderate-to-heavy, slightly dampen light
                corrected = raw_forecast * 1.1 if raw_forecast > 15 else raw_forecast * 0.9
            else:
                corrected = max(0, raw_forecast - 1.0)
                
        elif regime == "Break Monsoon":
            # Multiplicative bias correction with dry-day threshold
            dry_threshold = 2.0
            if raw_forecast < dry_threshold:
                corrected = 0.0
            else:
                corrected = raw_forecast * 0.7 # Models usually over-predict during breaks
                
        elif regime == "Monsoon Depression/Low":
            # Non-linear correction for heavy rainfall
            # Exponentially increase higher values as models often underpredict extremes
            if raw_forecast > 20:
                corrected = raw_forecast * (1 + 0.02 * (raw_forecast - 20))
            else:
                corrected = raw_forecast * 1.2
                
        elif regime == "Orographic Rainfall":
            # Elevation-dependent correction
            elevation = additional_params.get('elevation', 500)
            # Enhance rainfall proportionally to elevation up to a point
            enhancement = min(2.5, 1 + (elevation / 1000.0) * 0.5)
            corrected = raw_forecast * enhancement
            
        elif regime == "Coastal Rainfall":
            # Wind-direction dependent correction
            wind_dir = additional_params.get('wind_dir', 270) # Westerly default
            # If onshore (e.g., Westerly on West Coast 225-315), enhance
            if 225 <= wind_dir <= 315:
                corrected = raw_forecast * 1.3
            else:
                corrected = raw_forecast * 0.9
                
        elif regime == "Western Disturbance":
            # Temperature-dependent correction
            temp = additional_params.get('temperature', 20)
            if temp < 15: # Colder conditions might lead to more precipitation/snow
                corrected = raw_forecast * 1.2
            else:
                corrected = raw_forecast * 0.95
                
        return max(0.0, round(corrected, 1))

    def compute_heavy_rainfall_probability(self, corrected_forecast: float, threshold: float = 64.5) -> float:
        """
        Computes probability of exceeding heavy rainfall threshold using a Gamma distribution assumption.
        """
        if corrected_forecast <= 0:
            return 0.0
            
        # Assume a Gamma distribution centered around the corrected forecast
        # For prototype, shape parameter k varies with magnitude
        shape = max(1.5, corrected_forecast / 20.0) 
        scale = corrected_forecast / shape
        
        # Survival function (1 - CDF) gives probability of exceeding threshold
        prob = stats.gamma.sf(threshold, a=shape, scale=scale)
        
        return round(prob, 3)
