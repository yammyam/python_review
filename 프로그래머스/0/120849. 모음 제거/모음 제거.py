def solution(my_string):
    values = "aeiouAEIOU"
    return "".join([char for char in my_string if char not in values])