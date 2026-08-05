import turtle as t
import random as rd
from countryinfo import country_data
from saver import saveResult, generateRank


t.setup(1325, 735)
t.title('수도 맞추기 게임')
t.bgpic('world-map.gif')

t.ht()
t.penup()
t.speed(0)
t.shape('circle')
t.shapesize(0.5)
t.color('green')
t.goto(700, 350)
t.pensize(3)

n = 0
score = 0
randcountry = rd.sample(country_data, 10)
fileName = 'data.csv'


for i in range(len(randcountry)):
    q = t.textinput('수도 퀴즈', f'{n + 1}. {randcountry[n].get("국가")}의 수도를 입력하세요')
    t.up()
    if q in randcountry[n].get('수도'):
        t.color('white')
        score += 1
    else:
        t.color('red')

    t.goto(randcountry[n].get('좌표')[0], randcountry[n].get('좌표')[1] + 5)
    t.write(f'{randcountry[n].get("국가")} ({randcountry[n].get("수도")[0]})',\
            move=False,align='center',font=('Arial',10,'bold'))
    t.goto(randcountry[n].get('좌표')[0], randcountry[n].get('좌표')[1] - 2)
    t.pd()
    t.circle(2)
    n += 1


t.pu()
t.home()
t.color('#fff')
t.write(f'Score: {score}/10',\
        move=False, align='center', font=('Arial', 55, 'bold'))
saveResult(fileName, score * 10)
generateRank(fileName=fileName, reverse=True, unit='점', color='#fff')


t.listen()
t.done()
