'''
for i in [15, 2, 3]:
    print(i)

for i in range(2,11,2):
    print(i, end=" ")

for i in range(1,10,2):
    print(i, end=" ")

for i in range(5,-1,-1):
    print(i, end=" ")

for i in range(0, 9):
    print(i)

for i in range(5):
    print(i)

for hi in range(5, 8):
    print(hi)

for i in range(101):
    print(i)

count = 0
for i in range(10):
    count = count + 1
print(count)

for i in range(1, 20):
    print(19, "*", i, "=", 19 * i)

for i in range(3):
    print("I love Python!")

_sum = 0
for i in range(1, 11):
    _sum += i
print(f'합 : {_sum}')

num = 0
for i in range(2, 101, 2):
    num = num + i
print(f'1~100 사이의 수 중 짝수의 합 : {num}')

for i in range(1, 10):
    print("2*" + str(i) + "=" + str(2*i), end=" ")

start = int(input("시작 단 : "))
end = int(input("마지막 단 : "))
for i in range(start, end + 1):
    for ii in range(1, 10):
        print(str(i) + "*" + str(ii) + "=" + str(i * ii), end=" ")        
    print()

#★
Ln = int(input("사각형의 길이 : "))
for star in range(Ln):
    print("★" * Ln)

line = int(input("별트리 줄수 : "))
for tree in range(1, line + 1):
    print("★" * tree)

##●
##●★
##●★●
##●★●★
##●★●★●
line = int(input("업그레이드 트리 줄 개수 입력 : ")) #3
for i in range(line): #range(0,3,1)
    for ii in range(i+1): #range(0,1, 1)
        if ii % 2 == 0:
            print("●", end=" ")
        else:
            print("★", end=" ")
    print()


##while

i = 10
while i >= 1:
    print(i)
    i -= 1

i = 1
while i <= 10:
    print(str(i) + '년째 수감 중입니다.')
    i += 1
print('석방됨 ㅊㅋㅊㅋ')

i = 1
while True:
    print(i, '월 1만원을 입금했습니다.')
    if i == 12:
        print('입금 완료! 12만원을 수령하세요!')
        break
    i += 1

i = 1
_sum = 0
while True:
    _sum = _sum + i
    if i == 10:
        break
    i += 1
print(_sum)

star = int(input("층 입력 >>> "))
for i in range(1, star + 1, 1):
    print('★' * i)

q = int(input('1 + 2 = '))
while q != 3:
    q = int(input('땡! 다시 입력.. >> '))
print('정답!')

_sum = 0
x = 0
while True:
    x += 1
    _sum += x
    if _sum >= 3000:
        print("정답은", x)
        break
'
n = 13
print("=== 컴퓨터와 Up and Down Game ===")
while True:
    a = int(input("숫자 입력 >>> "))
    if a < n:
        print("UP")
    elif a > n:
        print("DOWN")
    else:
        print("정답!!")
        break

last = int(input('=== 369 Game === \n 마지막 숫자 입력 >>> '))
n = 1
while n < last + 1:
    if n % 3 == 0:
        print('짝', end = " ")
    else:
        print(n, end = " ")
    n += 1

## 어쩌구  = int(input("어쩌구 >>> "))
n  = int(input("숫자 입력 >>> "))
i = 1
count = 0
while i <= n:
    if n % i == 0:        
        if n == i:
            print(str(i), end = "")
        else:
            print(str(i), end = ", ")
        count += 1
    i += 1
print("\n" + str(n) + '의 약수는 총', str(count) + '개 입니다.')

# 2 => 1 ❎ 3 4 5 6 7 8 9
pick  = int(input("======남은자리 ======\n1 2 3 4 5 6 7 8 9\n자리 선택 >>> "))
n = 1
while n <= 9:
    if n == pick:
        print('❎', end = ' ')
    else:
        print(n, end = ' ')
    n += 1
'''
