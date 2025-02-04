def solution(s):
    answer = 0
    step = s.split(" ")
    for i in range(0 , len(step)):
        if(step[i] == "Z"):
            answer -= int(step[i-1])
        else:
            answer += int(step[i])
    return answer