def solution(box, n):
    arr = list(map(lambda x:x//n , box))
    answer = 1
    for i in arr:
        answer *=i
    return answer
# from functools import reduce
# def solution(box, n):
#     return reduce(lambda x,y :x*y,  list(map(lambda x:x//n , box))  )