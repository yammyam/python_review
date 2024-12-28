# def solution(array, n):
#     answer = 0
#     value = 101
#     for index, i in enumerate(array):
#         if abs(n-i) < value:
#             value = abs(n-i)
#             answer = index
#     return array[answer]

# 위의 코드 안되는 점 [23,21] 22 일때 결괏값 21이 도출이 안됨
def solution(array, n):
    answer = 0
    value = 101
    for index, i in enumerate(array):
        if abs(n-i) < value:
            value = abs(n-i)
            answer = index
        elif abs(n-i) == value:
            if i<array[answer]:
                answer = index
    return array[answer]