def solution(array):
    return "".join(map(str, array)).count("7")
# map, filter의 리턴값 이터러블
# join은 이터러블 한 것은 모두 적용 가능
# 문자열로 만들고 7의 갯수 세아리기