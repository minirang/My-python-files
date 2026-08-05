import turtle as t

def reset(pensize):
    t.penup()
    t.pensize(pensize)
    t.color('#fff')

t.setup(950, 550)
t.title("오징어게임 글자 그리기")
t.bgcolor('#000')
t.shape('turtle')
t.speed(6)
t.hideturtle() #

reset(15)
t.goto(-400, -100)
t.pendown()
t.forward(130)
t.penup()
t.forward(-40)
t.left(90)
t.pendown()
t.forward(60)

# 여기까지 오의 ㅗ 글자

t.penup()
t.pensize(18)
t.right(90)
t.pendown()
t.color('#eb4685')
t.circle(40)

# 여기까지 오의 ㅇ 글자

reset(15)
t.fd(70)
t.left(90)
t.fd(60)
t.right(90)
t.pendown()
t.fd(90)

t.penup()
t.pensize(18)
t.fd(-45)
t.left(90)
t.fd(5)
t.pendown()
t.color('#eb4685')
t.left(150)
for i in range(3):
    t.fd(80)
    t.left(120)
    
# 여기까지 징의 ㅈ

reset(15)
t.left(120)
t.fd(75)
t.left(90)
t.fd(55)
t.pendown()
t.left(180)
t.fd(105)


# 여기까지 징의 ㅣ

reset(15)
t.right(90)
t.fd(60)
t.left(90)
t.fd(50)
t.pendown()
t.circle(30)

# 여기까지 징 완료

reset(15)
t.goto(-85, 28)
t.pendown()
t.circle(35)
t.penup()
t.left(90)
t.fd(70)
t.pensize(18)
t.pendown()
t.fd(45)
t.left(90)
t.fd(75)
t.left(180)
t.fd(115)

# 여기까지 어 까지 완료

reset(16)
t.goto(15, -50)
t.left(90)
t.pendown()
t.fd(80)
t.right(110)
t.fd(105)
t.penup()
t.right(180)
t.fd(58)
t.right(70)
t.pendown()
t.fd(45)
t.left(90)
t.fd(45)
t.fd(-70)
t.penup()
t.right(90)
t.fd(25)
t.pendown()
t.left(90)
t.fd(70)
t.fd(-130)

# 여기까지가 게 글자

reset(15)
t.goto(245, 10)
t.pendown()
t.circle(30)
t.penup()
t.right(90)
t.pensize(17)
t.fd(45)
t.left(90)
t.pendown()
t.fd(75)
t.left(180)
t.fd(110)

# 여기까지 임의 이

t.penup()
t.pensize(18)
t.color('#eb4685')
t.fd(27)
t.pendown()
for i in range(4):
    t.fd(70)
    t.right(90)

# 끝

t.done()
