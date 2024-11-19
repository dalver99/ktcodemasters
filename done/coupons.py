def min_coupons(n):
    # 쿠폰 단위 리스트 (큰 단위부터)
    coupons = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = 0  # 쿠폰 개수

    for coupon in coupons:
        if n == 0:
            break
        count += n // coupon  # 현재 단위로 나누어 몇 장 사용할 수 있는지
        n %= coupon  # 남은 금액 계산

    return count

# 예제 입력
N = int(input())
print(min_coupons(N))
