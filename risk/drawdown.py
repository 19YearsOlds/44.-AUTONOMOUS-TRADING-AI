def check_drawdown(equity_curve, max_dd):
    peak = max(equity_curve)
    dd = (peak - euity_curve[-1]) / peak
    return dd < max_dd