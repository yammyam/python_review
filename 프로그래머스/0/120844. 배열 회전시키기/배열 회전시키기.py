def solution(numbers, direction):
    if direction == "right":
        return numbers[-1:] + numbers[:-1]
    return numbers[1:]+numbers[:1] 
# 배열+정수값 이 안됨 => 오류(TypeError)