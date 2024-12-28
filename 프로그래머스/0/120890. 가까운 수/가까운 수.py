# def solution(array, n):
#     answer = 0
#     value = 101
#     for index, i in enumerate(array):
#         if abs(n-i) < value:
#             value = abs(n-i)
#             answer = index
#     return array[answer]
def solution(array, n):
    answer = 0
    value = 101  # 초기값 설정
    for index, i in enumerate(array):
        if abs(n - i) < value:  # 더 가까운 수를 찾은 경우
            value = abs(n - i)
            answer = index
        elif abs(n - i) == value:  # 거리가 같은 경우 더 작은 수 선택
            if i < array[answer]:
                answer = index
    return array[answer]
