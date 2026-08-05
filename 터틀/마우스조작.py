import turtle as t
t.speed(0)
t.title('마우스 조작')
t.setup(700, 700)
t.pensize(2)
t.ht()
t.color("#000")

def catch(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.circle(5)
    print(x, y)


t.onscreenclick(catch)

t.listen()
t.done()
