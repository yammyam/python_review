def solution(dots):
    dots.sort(key=lambda x: x[0])
    
    one_side = abs(dots[0][1] - dots[1][1])
    other_side = abs(dots[0][0] - dots[2][0])
    
    return one_side * other_side
