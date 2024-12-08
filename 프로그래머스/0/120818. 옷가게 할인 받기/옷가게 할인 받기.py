def solution(price):
    if 0<=price<100_000:
        return price
    elif 100_000<=price<300_000:
        return int(price*0.95)
    elif 300_000<=price<500_000:
        return int(price*0.9)
    else:
        return int(price*0.8)