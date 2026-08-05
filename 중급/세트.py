set1 = {15, 25, "apple"}
print(set1)
set2 = set((["빨", "주", "노"]))
print(set2)
set3 = {10, 20, 30, 20} # 중복값 있을 시 삭제
print(set3)

set4 = {"가", "나", "다"} # in 사용 가능
print("가" in set4)
print("나" in set4)

## 요소 한 개 추가 : 세트명.add()
## 특정요소 삭제 : 세트명.remove()
## 요소 여러 개 추가 : 세트명.update() - 여러 개 자료는 대괄호로 묶음

set5 = {15, 25, 35}
print(set1)
set5.add(45)
print(set5)
set5.update([55, 65])
print(set5)
set5.remove(45)
print(set5)


color = ["가", "나", "다", "나"]
set6 = set(color)
print(set6)
uniqueColor = list(set2)
print(uniqueColor)
uniqueColor.sort()
print(uniqueColor)
print(f'첫번째 요소 : {uniqueColor[0]}')
print(f'마지막 요소 : {uniqueColor[-1]}')

## 두 집합의 교집합 : 세트1.intersection(세트2)
## 두 집합의 합집합 : 세트1.union(세트2)
## 두 집합의 차집합 : 세트1.defference(세트2)
