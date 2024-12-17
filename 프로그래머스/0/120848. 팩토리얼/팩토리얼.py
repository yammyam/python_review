def solution(n):
    answer = 1
    for i in range(1,3_628_800):
        answer*=i
        if n<answer:
            return i-1
 