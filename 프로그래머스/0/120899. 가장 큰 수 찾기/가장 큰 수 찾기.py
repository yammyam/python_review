def solution(array):
    standard = [array[0],0]
    for i, value in enumerate(array):
        if value > standard[0]:
            standard = [value, i]
    return standard

# def solution(array):
#     return [max(array), array.index(max(array))]