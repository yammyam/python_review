import math
def solution(slice, n):
    if slice < n:
        return math.ceil(n/slice)
    else:
        return 1