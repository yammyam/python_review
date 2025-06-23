def solution(phone_book):
    answer = True
    phone_dict = {}
    num_len = set()
    for number in sorted(phone_book, key=len):
        num_len.add(len(number))
        for length in num_len:
            if number[:length] in phone_dict:
                answer = False
                return answer
            elif len(number) == length:
                phone_dict[number] = 0
    return answer