from ingestion.market_feed import load_market_data
from features.technical import moving_average
from strategies.trend_following import TrendFollowing
from strategies.mean_reversion import MeanReversion
from strategies.ensemble import Ensemble
from execution.simulator import simulate
from ethics.disclaimer import DISCLAIMER

data = load_market_data("data/market_data.csv")
prices = data["price"]

tf = TrendFollowing()
mr = MeanReversion()
ensemble = Ensemble([tf, mr])

returns = []

for i in range(20, len(prices)):
    ma = prices[:i].mean()
    z = (prices[i] - ma) / prices[:i].std()

    features = {
        "price": prices[i],
        "ma": ma,
        "z": z
    }

    signal = ensemble.decide(features)
    ret = simulate(signal, prices[i] - prices[i-1])
    returns.append(ret)

print(DISCLAIMER)
print("Sharpe:", sum(returns))