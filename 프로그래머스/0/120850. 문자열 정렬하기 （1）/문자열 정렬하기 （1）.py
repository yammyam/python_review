def solution(my_string):
    answer = []
    for i in my_string:
        if i in "0123456789":
            answer.append(i)
    for i in range(0,len(answer)):
        answer[i] = int(answer[i])
    answer.sort()
    return answer