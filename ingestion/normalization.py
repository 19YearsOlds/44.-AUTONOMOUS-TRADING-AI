def normalize_prices(prices):
    mean = prices.mean()
    std = prices.std() + 1e-9
    return (prices - mean) / std