def solution(order):
    answer = str(order)
    c = 0
    for i in answer:
        if i in "369":
            c+=1
    return c