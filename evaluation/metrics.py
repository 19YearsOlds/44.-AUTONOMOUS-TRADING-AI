def sharpe(returns):
    mean = sum(returns) / len(returns)
    std = (sum((r - mean)**2 for r in returns) / len(returns))**0.5
    return mean / (std + 1e-9)