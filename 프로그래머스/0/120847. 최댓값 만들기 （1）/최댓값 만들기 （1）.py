def solution(numbers):
    numbers.sort()
    if(numbers[0]*numbers[1] < numbers[len(numbers)-2]*numbers[len(numbers)-1]):
        return numbers[len(numbers)-2]*numbers[len(numbers)-1]
    else:
        return numbers[0]*numbers[1]