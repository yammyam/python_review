def solution(n, numlist):
    return list(filter(lambda i:i%n == 0, numlist))