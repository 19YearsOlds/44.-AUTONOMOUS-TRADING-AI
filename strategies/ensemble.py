class Ensemble:
    def __init__(self, strategies):
        self.strategies = strategies
        self.weights = [1 / len(strategies)] * len(strategies)

    def decide(self, features):
        return sum(
            w * s.generate_signal(features)
            for w, s in zip(self.weights, self.strategies)
        )