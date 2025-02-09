def solution(id_pw, db):
    for item in db:
        if id_pw[0] == item[0] and id_pw[1] == item[1]:
            return "login"
        elif id_pw[0] == item[0] and id_pw[1] != item[1]:
            return "wrong pw"
    return "fail"