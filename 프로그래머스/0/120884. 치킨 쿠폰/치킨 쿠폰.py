def solution(chicken):
    coupon = chicken
    service = 0

    while coupon >= 10:
        # 10으로 나눈 몫을 정수로 변환
        new_service = int(coupon / 10)
        service += new_service
        # 남은 쿠폰 갱신 (남은 쿠폰 + 서비스 받은 치킨의 쿠폰)
        coupon = coupon % 10 + new_service

    return service
