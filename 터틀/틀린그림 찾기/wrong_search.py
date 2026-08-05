import turtle as t
from saver import saveResult, generateRank

t.title('틀린 그림 찾기')
t.setup(1220, 550)
t.bgpic("wrong_search.gif")
t.penup()
t.pensize(4)
t.speed(0)
t.color("red")
t.ht()

time = 30
left_time = time
isGaming = True
fileName = 'data.csv'
found = []
wrong_img = {0: [167, 207, -95, -66],\
             1: [82, 102, 134, 159],\
             2: [515, 537, -65, -56],\
             3: [358, 377, -41, -25],\
             4: [259, 274, -163, -153]}
             # 0. 이빨드러내면서 웃고있는애 모자 색깔
             # 1. 자루에 물건 하나
             # 2. 3번에 나무에서부터 나무 4번째 나무의 2층 색깔
             # 3. 노란색 눈 굴리고 있는애 위에 나무
             # 4. 누워있는애 장갑 색깔

score_pen = t.Turtle()
score_pen.hideturtle()
score_pen.color("purple")
score_pen.penup()
score_pen.goto(80, 232)
score_pen.write(left_time, False, 'center', ('', 25, 'bold'))



def catch(x, y):
    t.up()
    t.goto(x, y - 25)
    t.down()

    for n in range(5):
        if n in found:
            pass

        elif x >= wrong_img[n][0] and x <= wrong_img[n][1] and\
           y >= wrong_img[n][2] and y <= wrong_img[n][3]:
            t.circle(25)
            found.append(n)


def time_count():
    global left_time, isGaming

    if isGaming == True:
        left_time -= 1
        score_pen.clear()
        score_pen.write(left_time, False, 'center', ('', 25, 'bold'))
        t.ontimer(time_count, 1000)

        if left_time < 0:
            isGaming = False
            gameOver('timeout')
        
        if len(found) == len(wrong_img):
            isGaming = False
            gameOver('finish')


def gameOver(sort):
    t.setup(600, 550)
    if isGaming == False:
        t.bgpic('nopic')
        score_pen.clear()
        t.clear()
        if sort == 'timeout':
            score_pen.goto(0, 20)
            score_pen.color('red')
            score_pen.write('실패!', False, 'center', ('', 55, 'bold'))
            score_pen.goto(0, -50)
            score_pen.color('#000')
            score_pen.write(f'진행 시간 : {time - left_time}초', False, 'center', ('', 30, 'bold'))
            save()


        elif sort == 'finish':
            score_pen.goto(0, 20)
            score_pen.color('blue')
            score_pen.write('클리어!', False, 'center', ('', 55, 'bold'))
            score_pen.goto(0, -50)
            score_pen.color('#000')
            score_pen.write(f'진행 시간 : {time - left_time}초', False, 'center', ('', 30, 'bold'))
            save()


def save():
    saveResult(fileName=fileName, score=time-left_time)
    score_pen.clear()
    generateRank(fileName=fileName, reverse=False, unit='초', color='#000')


time_count()
t.onscreenclick(catch)
t.listen()
t.done()
