from strategies.base import Strategy

class MeanReversion(Strategy):
    def generate_signal(self, features):
        z = features["z"]
        if z > 1:
            return -1
        elif z < -1:
            return 1
        return 0