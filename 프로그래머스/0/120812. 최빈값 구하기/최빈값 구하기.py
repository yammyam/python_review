def solution(array):
    res = [0] * 1000
    
    for num in array:
        res[num] += 1
    
    max_val = max(res)
    count = 0
    answer = -1
    
    for i, val in enumerate(res):
        if val == max_val:
            answer = i
            count += 1
        if count >= 2:
            return -1
    
    return answer