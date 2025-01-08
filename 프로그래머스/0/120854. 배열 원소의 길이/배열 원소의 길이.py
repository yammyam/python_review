# def solution(strlist):
#     answer = [];
#     for i in strlist:
#         answer.append(len(i));
#     return answer
# map으로 한줄 
def solution(strlist):
    return list(map(lambda x: len(x),strlist))