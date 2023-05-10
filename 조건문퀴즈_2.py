# 1. 사용자로부터 가방, 시계 금액 입력받기
# 2. 합계 금액 10만원 이상 할인율 30%, 5 ~ 10만원 할인율 20%, 5만원 미만 할인율 10%

bag_price = int(input("가방의 금액을 입력해주세요. >>>"))
watch_price = int(input("시계의 금액을 입력해주세요. >>>"))

total_price = bag_price + watch_price

if total_price >= 100000:
    total_price = total_price * 0.7
elif total_price >= 50000:
    total_price = total_price * 0.8
else:
    total_price = total_price * 0.9

print("합계 금액은 :", total_price)