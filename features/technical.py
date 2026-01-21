import numpy as np

def moving_average(prices, window):
    return prices.rolling(window).mean()
def momentum(prices, window):
    return prices.diff(window)