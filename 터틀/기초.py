import turtle as t
import random as r
import time as tm

'''
t.setup(500, 500)
t.title('터틀 연습')
t.bgcolor('#000')

t.shape('turtle')
t.color('#fff')
t.speed(3)
t.pensize(1)
t.shapesize(1)

t.goto(r.randint(-250, 250), r.randint(-250, 250))
t.forward(50)
t.right(90)
t.left(60)
t.penup()
t.pendown()
t.circle(10)
'''
t.setup(500, 500)
t.title('터틀로 도형그리기')
t.shape('turtle')
t.penup()
t.goto(r.randint(-100, 100), r.randint(-100, 100))
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120)

























t.done()
