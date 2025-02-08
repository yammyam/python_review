def solution(n):
    result = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            result.append(divisor)
            while n % divisor == 0:
                n //= divisor
        else:
            divisor += 1

    return result