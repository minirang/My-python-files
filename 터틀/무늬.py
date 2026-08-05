import random as rd
import turtle as t

t.bgcolor('black')
t.speed(0)
t.ht()

# 태극무늬
'''for x in range(200):
    if x % 3 == 0:
        t.color('red')

    elif x % 3 == 1:
        t.color('yellow')

    elif x % 3 == 2:
        t.color('blue')

    t.fd(x * 2)
    t.lt(119)'''

# 원무늬
for x in range(250):
    if x % 3 == 0:
        t.color('red')

    elif x % 3 == 1:
        t.color('yellow')

    elif x % 3 == 2:
        t.color('blue')

    t.circle(x / 2)
    t.fd(x * 2)
    t.lt(119)

t.done()
