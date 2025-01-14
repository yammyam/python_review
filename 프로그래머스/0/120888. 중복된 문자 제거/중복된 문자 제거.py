def solution(my_string):
    return "".join(dict.fromkeys(my_string))
# 딕셔너리에 넣어 중복된거 자체제거