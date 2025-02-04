def solution(s):
    stack = []
    step = s.split(" ")
    for i in step:
        if(i == "Z"):
            if stack:
                stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)