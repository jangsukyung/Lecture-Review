# 리스트 생성하기
animals = ['사자', '호랑이', '고양이', '강아지']

# 데이터 접근하기
name = animals[0] # 0번째 인덱스

# 데이터 추가하기
animals.append('하마')
animals.append(1) # 같은 타입이 아니어도 가능

# 데이터 삭제하기
del animals[-1] # Delete, 마지막 데이터 삭제

# 리스트 슬라이싱
slicing = animals[1:3]

# 리스트 길이
length = len(animals)

# 리스트 정렬하기
animals.sort(reverse = True) # reverse : 내림차순

print(animals)