from strategies.base import Strategy

class TrendFollowing(Strategy):
    def generate_signal(self, features):
        ma = features["ma"]
        price = feature["price"]
        return 1 if price > ma else -1