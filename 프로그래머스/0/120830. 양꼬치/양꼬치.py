def solution(n, k):
    discount = n//10
    return (n*12000) + (2000*(k - discount))