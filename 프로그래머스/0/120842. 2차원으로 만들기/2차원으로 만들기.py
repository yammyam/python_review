def solution(num_list, n):
    result = [num_list[i:i+n] for i in range(0, len(num_list), n)]
    return result