def solution(my_string, n):
    list =  [ i*n for i in my_string]
    answer = ""
    for i in list:
        answer += i
    return answer