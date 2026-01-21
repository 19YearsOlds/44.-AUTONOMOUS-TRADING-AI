def update_weights(weights, rewards, lr):
    return [
        w + lr * r
        for w, r in zip(weights, rewards)
    ]