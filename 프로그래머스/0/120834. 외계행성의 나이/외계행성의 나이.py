def solution(age):
    answer = ""
    list = "abcdefghij"
    for i in str(age):
        answer += list[int(i)]
    return answer