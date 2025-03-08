# def solution(spell, dic):
#     # 스펠 돌면서 첫번째 요소를 돌리면서 dic 단어 첫번재에 하나만 들어있는지를 검색
#     new_arr = list(filter(lambda x : len(x) == len(spell),dic))
#     for i in range(0,len(new_arr)):
#         if new_arr[i].count(spell[i])!=1:
#             return 2
#     return 1
def solution(spell, dic):
    return 1 if any(set(spell) == set(word) for word in dic) else 2
