'''
pumpkin = (1,5,2,3,6)
bigest = max(pumpkin)
smallest = min(pumpkin)
print(bigest, smallest)

print(sum((1,2,3,4,5)))
print(len("Triangle"))

my_list = [1,2,3,4,5]
var1 = sum(my_list)
var2 = len(my_list)
var3 = int(var1 / var2)
print(var1, var2, var3)

def my_func(a, b):
    c = 2 * (a + b)
    return c
print(my_func(3, 4))

def my_star(a):
    return '*' * a
print(my_star(7))

x = 'Hi!' # 전역변수
def my_func():
    y = 'Hello!'
    print(x)
my_func() # 함수 안에서 사용해도 OK
print(x) # 함수 밖에서 사용해도 OK
print(y) # 함수 밖에서 사용하면 오류 발생

greeting = '밥 먹었니?'

print('서울:', greeting)
def busan():
    greeting = '밥 뭇나?'
    print('부산:', greeting)
busan()
print(greeting) # 전역
'''
def jjackhole(n):
    if n % 2 == 0:
        return '짝'
    else:
        return '홀'
num = int(input('수 하나 입력 >>> '))
print(f'{jjackhole(num)}수')



