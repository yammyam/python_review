def solution(n):
    return list(filter(lambda x: x%2 != 0, range(1,n+1)))