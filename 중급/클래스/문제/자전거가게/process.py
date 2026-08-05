from bicycle import Bicycle
from shop import Shop

def customer():
    while True:
        if ms_shop.list_stock(False) == 'empty':
            ms_shop.list_stock(True)

        else:
            try:
                ms_shop.list_stock(True)
                q = int(input('구매할 상품의 번호 입력 (또는 아무 문자로 종료) >> '))
                if q > len(ms_shop.stock):
                    raise IndexError

                q2 = int(input('수량? (또는 아무 문자로 종료) >> '))
                if q2 == 0:
                    raise IndexError

                ms_shop.sell(q-1, q2)

            except ValueError:
                break

            except IndexError:
                print('없는 자전거를 선택했거나 수량의 범위를 벗어났습니다.\n')


def pw():
    try:
        file = open('pw.txt', 'r')
        password = file.read()
        file.close()

        pw = input('비번 입력 >> ')
        if pw == password:
            return 'success'

        else:
            print('틀렸습니다. 뒤로 돌아갑니다.\n')

    except FileNotFoundError:
        print('비밀번호가 저장된 파일을 찾을 수 없습니다. 뒤로 돌아갑니다.\n')


def admin():
    if pw() == 'success':
        while True:
            try:
                q = int(input(\
                    '작업 선택 [0: 자전거 등록, 1: 매출 보기, 2: 재고보기, 3: 나가기] >> '))
                if q == 3:
                    break

                if q == 2:
                    ms_shop.list_stock(True)

                elif q == 1:
                    ms_shop.print_revenue()

                elif q == 0:
                    bicycle = Bicycle(input('자전거 색깔? >> '),\
                                       int(input('자전거 가격? (숫자만) >> ')),\
                                      input('자전거 이름? >> '),\
                                      int(input('자전거 수량? (숫자만) >> ')))
                    bicycle.__str__()

                    ms_shop.add(bicycle.name, bicycle.price, bicycle.quantity)
                    print(f'{bicycle.name}이/가 {bicycle.quantity}개 등록됨\n')

            except ValueError:
                pass


# 가게 생성
ms_shop = Shop()
ms_shop.__init__()

print('')
while True:
    q = input('관리자 또는 고객 입력 >> ')
    if q == '관리자':
        admin()

    elif q == '고객':
        customer()
