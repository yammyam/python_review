def solution(nlist):
    return [sum([1 for i in nlist if i % 2 == 0]), sum([1 for i in nlist if i % 2 != 0])]
