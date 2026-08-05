import turtle as t

'''
turtle 방향
↑ = 90
↓ = 270
← = 180
→ = 0
'''
t.speed(8)
t.title('어버이날 카드')
t.bgcolor('#fff')
t.setup(900, 600)
t.ht()
t.pu()

t.goto(-200, -250)
t.color('green')
t.setheading(9)

t.pensize(10)
t.pd()
t.circle(250, 75)

t.color('red')
t.pensize(3)

for i in range(150):
    t.fd(i)
    t.left(65)
t.fd(16)

t.pu()
t.color('black')
t.goto(-210, 170)
t.write('🎉(경)  어버이날  (축)🎉', False, 'left', ('', 30))
t.goto(-170, 125)
t.write('부모님, 사랑하고 감사합니다.', False, 'left', ('', 20, 'bold'))

t.color('pink')
t.goto(-330, -60)
t.write('♥', False, 'left', ('', 130))
t.goto(270, -50)
t.write('♥', False, 'left', ('', 120))


t.done()
