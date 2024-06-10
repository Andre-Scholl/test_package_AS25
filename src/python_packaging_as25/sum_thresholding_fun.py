import numpy as np

def sum_thresholding_fun(x, threshold):
    """Threshold array and sum positive elemens"""
    
    x = np.round(x)
    x_th = x > threshold
    out = np.sum(x_th)
    
    return out

my_array = np.array([0.1, 0.4, 0.3, 0.9, 1.1, 1.2])

out = sum_thresholding_fun(my_array, 0)

print(out)