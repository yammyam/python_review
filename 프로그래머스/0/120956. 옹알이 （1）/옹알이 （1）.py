def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        init = word
        
        for c in can:
            if c in init:
                init = init.replace(c, "X")  # 할 수 있는 단어는 X로 치환
        
        init = init.replace("X", "")  # X를 모두 공백으로 치환하고 나서
        if len(init) == 0:  # 공백이 되면 answer에 추가
            answer += 1
    
    return answer