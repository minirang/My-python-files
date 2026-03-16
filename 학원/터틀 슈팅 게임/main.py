import turtle
import random
import time

# 기본설정
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=700)
screen.title("터틀 슈팅 게임")
screen.tracer(0) # 화면에 나오는 모든 개체의 동작을 자연스럽게 해줌

# 플레이어 생성
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.setheading(90)
player.goto(0, -250)

# 점수펜 생성
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(-255, 300)
score_pen.write("Score: 0", font=("Arial", 14, "normal"))

# 변수들
score = 0 # 점수
gaming = True
bullets = [] # 총알리스트
enemies = [] # 적리스트

# 플레이어 이동 함수
def move_left():
    x = player.xcor()
    if x > -270:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 270:
        player.setx(x + 20)

# 총알 발사 함수   
def shoot():
    bullet = turtle.Turtle()
    bullet.shape("circle")
    bullet.color("yellow")
    bullet.penup()
    bullet.goto(player.xcor(), player.ycor())
    bullets.append(bullet)

# 적 생성 함수
def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    x = random.randint(-260, 260)
    enemy.goto(x, 300)
    enemies.append(enemy)

# 충돌 체크 함수
def is_collision(t1, t2):
    distance = t1.distance(t2)
    return distance < 20

# 키 설정
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(shoot, "space")

# 게임 루프
def start():
    global gaming
    if gaming == True:
        global score
        screen.update()

        # 랜덤 적 생성
        if random.randint(1, 45) == 1:
            create_enemy()

        # 총알 이동
        for bullet in bullets[:]:
            bullet.sety(bullet.ycor() + 20)
            if bullet.ycor() > 350:
                bullet.hideturtle()
                bullets.remove(bullet)

        # 적 이동
        for enemy in enemies[:]:
            enemy.sety(enemy.ycor() - random.randint(3, 7))

            # 플레이어와 충돌
            if is_collision(enemy, player):
                print("게임 오버")
                screen.bye()

            # 총알과 충돌
            for bullet in bullets[:]:
                if is_collision(enemy, bullet):
                    enemy.hideturtle()
                    bullet.hideturtle()
                    enemies.remove(enemy)
                    bullets.remove(bullet)

                    score += 10
                    score_pen.clear()
                    score_pen.write(f"Score: {score}", font=("Arial", 14, "normal"))

        screen.ontimer(start, 20) # 재귀함수 (20 밀리초 단위로 실행)

start()
