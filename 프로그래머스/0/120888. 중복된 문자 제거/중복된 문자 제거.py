# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer += i
#     return answer
def solution(my_string):
    return "".join(dict.fromkeys(my_string))
# 딕셔너리에 넣어 중복된거 자체제거