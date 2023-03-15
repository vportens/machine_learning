import numpy as np

def coef_det(y, pred):
    u = np.power((y - pred), 2).sum()
    v = np.power((y - y.mean()), 2).sum()
    return 1 - u/v