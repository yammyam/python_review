def solution(score):
    avg = [sum(s) / 2 for s in score]
    return [sum(a < b for b in avg) + 1 for a in avg]
