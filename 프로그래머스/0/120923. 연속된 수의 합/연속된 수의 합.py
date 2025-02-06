def solution(num, total):
    answer = []
    
    is_even = num % 2 == 0
    
    if is_even:
        standard = (total - num / 2) / num
    else:
        standard = total / num
    
    if is_even:
        start = int(standard - num / 2 + 1)
        end = int(standard + num / 2)
    else:
        start = int(standard - (num // 2))
        end = int(standard + (num // 2))
    
    for i in range(start, end + 1):
        answer.append(i)
    
    return answer
