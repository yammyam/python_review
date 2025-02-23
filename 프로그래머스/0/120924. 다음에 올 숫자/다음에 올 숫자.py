def solution(common):
    # 등차수열인지 확인
    same_minus = common[1] - common[0] == common[2] - common[1]
    if same_minus:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] / common[0])