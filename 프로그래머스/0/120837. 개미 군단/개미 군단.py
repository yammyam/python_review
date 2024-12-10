def solution(hp):
    answer = 0
    resHp = hp
    if resHp//5 != 0:
        answer += resHp//5
        resHp = resHp%5
    if resHp//3 !=0:
        answer += resHp//3
        resHp = resHp%3
    answer+=resHp//1
    return answer