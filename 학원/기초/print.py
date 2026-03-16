'''
print(['Hello', 12345])
print("10+3 = ", 10+3)
print("10-3 = ", 10-3)
print("10*3 = ", 10*3)
print("10/3 = ", 10/3)
print("10**3 = ", 10**3)
print("10%3 = ", 10%3)
print("(10+3)*2 = ", (10+3)*2)
pi=3.14159265358979
print(pi)
pi=pi+1
print(pi)
pi=3.14159265358979
pi*=2
print(pi)
끝'''

a = int(input("첫번째 수 입력 >>> "))
b = int(input("두번째 수 입력 >>> "))
c = int(input("세번째 수 입력 >>> "))
print(a, "+", b, " = ", a+b)
print(a, "-", b, " = ", a-b)
print(a, "*", b, " = ", a*b)
print(a, "/", b, " = ", a/b)
print(a, "**", b, " = ", a**b)
print(a, "%", b, " = ", a%b)
print("(", a, "+", b, ")", "*", c, " = ", ((a+b)*c))
