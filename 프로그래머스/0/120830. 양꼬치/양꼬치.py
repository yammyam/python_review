def solution(n, k):
    discount = int(n/10)
    return (n*12000) + (2000*(k - discount))