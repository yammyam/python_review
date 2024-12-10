def solution(order):
    answer = str(order)
    count = 0
    for i in answer:
        if i in "369":
            count+=1
    return count