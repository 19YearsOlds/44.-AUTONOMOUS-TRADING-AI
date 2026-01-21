import numpy as np

def volatility(prices, window):
    return prices.rolling(window).std()