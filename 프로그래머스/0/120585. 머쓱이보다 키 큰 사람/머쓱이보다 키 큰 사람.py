def solution(array, height):
    count =  sum(x > height for x in array)
    return count