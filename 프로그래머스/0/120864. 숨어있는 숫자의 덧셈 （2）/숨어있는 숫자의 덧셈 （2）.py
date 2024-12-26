import re
def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    total = sum(map(int, numbers))
    return total
# 정규식사용
# 정규식말고 ?