from collections import Counter

def solution(array):
    count = Counter(array)
    max_val = max(count.values())
    mode = [k for k, v in count.items() if v == max_val]
    return mode[0] if len(mode) == 1 else -1
