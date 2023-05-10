# 9만원이상 : 매도, 8 ~ 9만원 : 대기중, 8만원 미만 : 매수
price = int(input("삼성전자의 현재 가격을 입력해주세요. >>>"))

if price >= 90000:
    print("매도합니다.")
elif price >= 80000:
    print("대기중입니다.")
else:
    print("매수합니다.")