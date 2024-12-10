def solution(my_string):
    answer = []
    for i in my_string:
        if i in "0123456789":
            # 해당 문자열이 isdigit()함수로 숫자인지 판별가능
            answer.append(i)
    for i in range(0,len(answer)):
        answer[i] = int(answer[i])
    return sorted(answer)