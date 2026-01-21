import numpy as np

def detect_regime(vol):
    if vol > 1.5:
        return "high_vol"
    return "normal"