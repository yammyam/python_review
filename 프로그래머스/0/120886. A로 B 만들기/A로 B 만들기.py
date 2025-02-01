# def solution(before, after):
#     return 1 if "".join(reversed(before)) == after else 0
def solution(before, after):
    for i in before:
        if(before.count(i) != after.count(i)):
            return 0
    return 1
