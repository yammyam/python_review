def solution(box, n):
    arr = list(map(lambda x:x//n , box))
    answer = 1
    for i in arr:
        answer *=i
    return answer