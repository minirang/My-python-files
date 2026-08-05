import turtle as t
'''
사용시
from saver import saveResult, generateRank
'''


def saveResult(fileName, score):
    q = t.textinput('랭킹에 등록할 이름 입력', '이름 입력')
    target = open(fileName, 'a')
    target.write(f'{score},{q}\n')
    target.close()


def generateRank(fileName, reverse, unit, color):
    ranking = ()
    target = open(fileName, 'r')
    data = list(target.readlines())
    target.close()
    
    length = len(data)
    for i in range(length):
        data.append(data[0].split(','))
        data.pop(0)
        data[-1][-1] = data[-1][-1].replace('\n', '')
        data[-1][0] = int(data[-1][0])

    data.sort(reverse=reverse)

    t.clear()
    ranking = t.Turtle()
    ranking.ht()
    ranking.up()
    ranking.color(color)
    ranking.goto(0, 65)
    ranking.write(f'랭킹',\
        move=False, align='center', font=('Arial', 68, 'bold'))

    if len(data) >= 1:
        ranking.goto(0 ,-25)    
        ranking.write(f'👑1등: {data[0][-1]}, {data[0][0]}{unit}',\
            move=False, align='center', font=('Arial', 43, 'bold'))

    if len(data) >= 2:
        ranking.goto(0, -115)
        ranking.write(f'2등: {data[1][-1]}, {data[1][0]}{unit}',\
            move=False, align='center', font=('Arial', 43, 'bold'))

    if len(data) >= 3:
        ranking.goto(0, -215)
        ranking.write(f'3등: {data[2][-1]}, {data[2][0]}{unit}',\
            move=False, align='center', font=('Arial', 43, 'bold'))


#ranking = (f'============= 랭킹 =============\n👑1등: {data[0][-1]}, {data[0][0]}\n\n  2등: {data[1][-1]}, {data[1][0]}\n\n  3등: {data[2][-1]}, {data[2][0]}\n================================')
#return ranking
