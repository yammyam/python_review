def solution(sides):
    return 1 if sum(sorted(sides)[:2]) > max(sides) else 2
