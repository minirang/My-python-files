## 튜플 만들기

tp = (1,3,5,7,9) # 튜플
print(tp)

color = ['빨', '주', '노'] # 리스트를 튜플로
color = tuple(color)
print(color)

x = 1, 2 # 변수의 값을 1개 이상 부여시 튜플로 저장
print(x)

y = (14, 25, (35, 45)) # 튜플 안에 튜플 가능
print(y)


## 인덱싱과 슬라이싱 (리스트와 동일)

##tp = (1,3,5,7,9)
print(tp[0])
print(tp[-1])
print(tp[1:])
print(tp[:2])
print(tp[:])
print(len(tp))
