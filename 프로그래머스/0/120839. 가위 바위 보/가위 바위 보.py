def solution(rsp):
    map = {
        "2":"0",
        "0":"5",
        "5":"2"
    }
    answer = ""
    for i  in  rsp:
        answer += map[i]
    return answer