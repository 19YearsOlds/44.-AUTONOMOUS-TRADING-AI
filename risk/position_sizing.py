def size(signal, confidence, max_pos):
    return max(-max_pos, min(max_pos, signal * confidence))