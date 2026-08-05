import turtle as t

def turn_right():
    t.setheading(0)
    t.fd(10)


def turn_up():
    t.setheading(90)
    t.fd(10)


def turn_left():
    t.setheading(180)
    t.fd(10)


def turn_down():
    t.setheading(270)
    t.fd(10)


def blank():
    t.clear()


t.shape('turtle')
t.speed(0)
t.title('키보드 조작')
t.setup(700, 700)

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")

t.listen()
t.done()
