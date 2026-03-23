import random as rd
import time as tm
'''
def order(menu):
    if menu == 1:
        print('아메리카노 가격 : 2500원')
    elif menu == 2:
        print('카푸치노 가격 : 3500원')
    elif menu == 3:
        print('바닐라라떼 가격 : 4500원')
    else:
        print('없는 메뉴')

print("가격을 확인해보세요\n====== Menu ======\n1. 아메리카노\n2. 카푸치노\n3. 바닐라라떼\n==================\n")
menu_input = int(input("1, 2, 3번 메뉴 중 하나 입력 >>> "))
order(menu_input)
'''

def menu():
    rice = ['참치김밥', '오므라이스', '제육덮밥', '설렁탕', '추어탕', '된장찌개', '김치찌개', '봄동비빔밥', '김치볶음밥', '초밥']
    bread = ['치즈버거', '햄 샌드위치', '머시룸 파니니', '마르게리타 피자']
    etc = ['쌀국수', '떡볶이', '샤부샤부', '파스타', '훠궈', '마라샹궈', '딤섬', '짜장면', '빵에 딸기잼에 우유', '다이어트를 핑계로 안먹는다']
    lunch_menu = int(input("원하는 음식 종류 입력\n밥 종류: 1, 빵 종류: 2, 기타 등등: 3 >>> "))
    if lunch_menu > 3:
        print('없는 메뉴')
    else:
        for i in range(3, 0, -1):
            print(i)
            tm.sleep(1)

    if lunch_menu == 1:
        print(rd.choice(rice))
    elif lunch_menu == 2:
        print(rd.choice(bread))
    elif lunch_menu == 3:
        print(rd.choice(etc))
menu()
