def solution(s):
    return ''.join(sorted(c for c in s if s.count(c) == 1))
# count 사용