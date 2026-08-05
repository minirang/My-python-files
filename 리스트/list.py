'''
s = 'Ready'
li = [1,2,3]
print(s[1])
print(li[0])

animal = ['토끼', '멜론', '홍학']
animal[1] = '도마뱀'
print(animal)

beta = [2, 4, 6, 8, 10, 12, 14, 16]
print(beta[2:5])

bag1 = ['은', '은', '다이아', '은', '은', '은', '은']
jewel1 = bag1[2]
bag2 = ['은', '은', '금', '금', '금', '은', '은','은']
jewel2 = bag2[2:5]
print('가방 안 제일 비싼 보석', jewel1)
print('가방 안 제일 비싼 금속', jewel2)

cart = ['우유', '설탕']
cart.append('새우깡')
print(cart)
cart.insert(0, '감자깡')
print(cart)

## append
line_up = []
line_up.append('거북이')
line_up.append('홍학')
line_up.append('토끼')
print(line_up)
## insert
line_up.insert(1, '도도새')
print(line_up)
## remove
line_up.remove('도도새')
print(line_up)
## sort
line_up.sort()
print(line_up)

a = [6, 2, 4, 1]
a.sort()
print(a)
##
b = ['carrot', 'apple', 'banana']
b.sort()
print(b)

## 문자열
a = 'once'
print(a[1])
print(a[-1]) # 뒤에서 1번째
## 리스트
a = ['t', 'w', 'i', 'c', 'e']
print(b[2:4])
print(b[:3]) # 처음부터 3 미만
print(b[:]) #전체 다 => 't', 'w', 'i', 'c', 'e'
## 튜플
c = (1, 2, 3, 4, 5)

bag1 = ['은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '다이아', '은']
jewel1 = bag1[-2]
bag2 = ['은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '금', '금', '금', '금', '금', '금', '금', '금', '금']
jewel2 = bag2[-9:]
print('가방 안 가장 비싼 보석', jewel1)
print('가방 아 가장 금빛 보석', jewel2)

출석자 = ['도도새', '애벌레', '토끼', '모자장수', '체셔']
print('토끼' in 출석자) # '토끼' 원소가 출석자 안에 들어 있는지 확인
##
a = 'once'
print('o' in a) #True
print('z' in a) #False
##
print(len(a)) ## 4

b = ['t', 'w', 'i', 'c', 'e']
print(len(b)) ## 5

my_list = ['Apple', 'Banana', 'Chamwae', 'Durian']
my_var = 'egg' in my_list
print(my_var)

my_str = 'Impossible'
my_var = len(my_str)
print(my_var)

c = ['t', 'w', 'i'] + ['c', 'e']
print(c)
##
d = ['Hi'] * 3
print(d)

my_list = [3, 6, 9]
my_var = my_list * 3
print(my_var)

item1 = '완전 좋고'
item2 = '빛나며'
item3 = '손에 착착 감기는'
space = ' '
weapon = item1 + space + item2 + space + item3 + ' 무기'
print(weapon)

train = ['성진', '찬경', '준영']
print(train)
train.append('주아')
print('서울역 도착함.  //', train)
train.insert(0, '동빈')
print('대전역 도착함.  //', train)
train.sort()
print('부산역 도착함.  //', train)
print('오늘도 코딩별 기차 이용 ㄳㄳ.')

fruits = ['바나나', '딸기', '두리안', '망고'] ## ['바나나', '두리안', '망고']
print(fruits)
if '딸기' in fruits:
    fruits.remove('딸기')
    print(fruits)
else:
    print('딸기는 fruits 안에 없음.')

my_list = [1, 2, 2, 3, 3, 3]
var = my_list.count(3)
my_list.pop(2)
my_list.pop(3)
my_list.pop(3)
print(my_list)

my_str = 'Ialikeayou'
print(my_str.split('a'))

my_str = '가,나,다,라,마' ##쉼표배열
print(my_str.split(','))

dessert = ['Coffee', 'Donut']
print('&'.join(dessert)) ## &로 붙이기
dessert = ['ice', 'cream']
print(''.join(dessert))

my_list = ['Seeing', 'is', 'Believing']
var = ' '.join(my_list)
print(var)

n = int(input('수 입력 >>> '))
lyrics = '바람이,분다,바람이,불어,연평,바다에,어허허얼싸,돈바람,분다,얼써,\
좋네,아,좋네,군밤이요,에헤라,생률,밤이로구나,달도,밝다,달도,밝아,우주,강산에,\
어허어얼싸,저,달이,밝아,얼싸,좋네,아,좋네,군밤이요,에헤라,생률,밤이로구나'
lyrics_list = lyrics.split(',')
print(lyrics_list.count('바람이'))
print(lyrics_list[2])

my_list = [2,3,4,5]
my_list.pop()
print(my_list)

my_list = [1,2,3,4,5]
print(my_list.pop(3))
print(my_list)

my_seq = [22,22,22,4,4,]
print(my_seq.count(22))

my_list = [1,2,2,3,3,3]
var = my_list.count(3)
my_list.pop(2)
my_list.pop(3)
my_list.pop(3)
print(my_list)

my_str = 'Ialikeayou'
print(my_str.split('a'))

n = input("두 수 입력 (단, 두 수는 공백을 기준으로 분리할것) >>> ")
print(int(n.split()[0]) + int(n.split()[1]))

dessert = ["Coffee", "Donut"]
print(" & ".join(dessert))
thing = ["water", "fall"]
print("".join(thing))

my_list = ['Seeing', 'is', 'Believing']
var = ' '.join(my_list)
print(var)
'''





















