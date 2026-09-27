import numpy as np
import pandas as pd
from typing import Dict, List, Any, Tuple

class ForecastVerifier:
    """
    Computes verification metrics for rainfall forecasts.
    """
    
    def __init__(self):
        pass
        
    def _contingency_table(self, observed: np.ndarray, forecast: np.ndarray, threshold: float) -> Tuple[int, int, int, int]:
        """Calculates Hits (a), False Alarms (b), Misses (c), Correct Negatives (d)."""
        obs_event = observed >= threshold
        fcst_event = forecast >= threshold
        
        hits = np.sum(obs_event & fcst_event)
        false_alarms = np.sum(~obs_event & fcst_event)
        misses = np.sum(obs_event & ~fcst_event)
        correct_negatives = np.sum(~obs_event & ~fcst_event)
        
        return hits, false_alarms, misses, correct_negatives

    def _fss_simplified(self, observed: np.ndarray, forecast: np.ndarray, threshold: float) -> float:
        """Simplified Fractions Skill Score (without spatial neighborhood for prototype)."""
        obs_event = (observed >= threshold).astype(float)
        fcst_event = (forecast >= threshold).astype(float)
        
        mse = np.mean((fcst_event - obs_event) ** 2)
        mse_ref = np.mean(fcst_event ** 2) + np.mean(obs_event ** 2)
        
        if mse_ref == 0:
            return 1.0
        return 1.0 - (mse / mse_ref)

    def verify(self, observed: np.ndarray, forecast: np.ndarray, 
               thresholds: List[float] = [2.5, 15.6, 64.5, 115.6, 204.5]) -> Dict[str, Any]:
        """
        Computes continuous and categorical verification metrics.
        """
        observed = np.asarray(observed)
        forecast = np.asarray(forecast)
        
        # Continuous metrics
        rmse = np.sqrt(np.mean((forecast - observed) ** 2))
        corr = np.corrcoef(observed, forecast)[0, 1] if len(observed) > 1 else 0
        
        results = {
            "continuous": {
                "RMSE": round(float(rmse), 3),
                "Correlation": round(float(corr), 3)
            },
            "categorical": {}
        }
        
        # Categorical metrics per threshold
        for t in thresholds:
            a, b, c, d = self._contingency_table(observed, forecast, t)
            n = a + b + c + d
            
            pod = a / (a + c) if (a + c) > 0 else 0
            far = b / (a + b) if (a + b) > 0 else 0
            csi = a / (a + b + c) if (a + b + c) > 0 else 0
            bias = (a + b) / (a + c) if (a + c) > 0 else 0
            
            # ETS
            ar = (a + b) * (a + c) / n if n > 0 else 0
            ets_denom = a + b + c - ar
            ets = (a - ar) / ets_denom if ets_denom > 0 else 0
            
            # Simplified FSS
            fss = self._fss_simplified(observed, forecast, t)
            
            results["categorical"][f"Threshold_{t}"] = {
                "POD": round(pod, 3),
                "FAR": round(far, 3),
                "CSI": round(csi, 3),
                "ETS": round(ets, 3),
                "Bias_Score": round(bias, 3),
                "FSS_simplified": round(fss, 3),
                "Hits": int(a),
                "False_Alarms": int(b),
                "Misses": int(c)
            }
            
        return results

    def compare_forecasts(self, observed: np.ndarray, raw_forecast: np.ndarray, 
                          corrected_forecast: np.ndarray, 
                          thresholds: List[float] = [2.5, 15.6, 64.5, 115.6]) -> Dict[str, Any]:
        """
        Compares raw and corrected forecasts, showing the improvement.
        """
        raw_metrics = self.verify(observed, raw_forecast, thresholds)
        corrected_metrics = self.verify(observed, corrected_forecast, thresholds)
        
        comparison = {
            "Raw": raw_metrics,
            "Corrected": corrected_metrics,
            "Improvement": {
                "RMSE_reduction_pct": 0,
                "Correlation_increase": 0
            }
        }
        
        # Calculate % improvement for continuous
        raw_rmse = raw_metrics["continuous"]["RMSE"]
        corr_rmse = corrected_metrics["continuous"]["RMSE"]
        if raw_rmse > 0:
            comparison["Improvement"]["RMSE_reduction_pct"] = round((raw_rmse - corr_rmse) / raw_rmse * 100, 2)
            
        comparison["Improvement"]["Correlation_increase"] = round(
            corrected_metrics["continuous"]["Correlation"] - raw_metrics["continuous"]["Correlation"], 3
        )
        
        return comparison
