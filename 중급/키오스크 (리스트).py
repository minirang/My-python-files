menu = ['치즈버거', 3000, '불고기버거', 4000, '채소버거', 3500, '콜라', 2000, '사이다', 2000]
order = []
pay = 0
num = 1

print('메뉴 출력 ================================\n')
for i in range(0, len(menu), 2):
    print(f'{num}. {menu[i]} ------ {menu[i + 1]}원')
    num += 1
print('\n==========================================\n\n')

while True:
    q = input('주문할 메뉴의 번호를 입력하세요 >> ')
    order.append((int(q) - 1) * 2)
    q = input('수량을 입력하세요 >> ')
    order.append(int(q))

    q = input('추가 주문하시겠습니까? (추가주문시 0 입력) >> ')
    if int(q) > 0:
        break

for i in range(0, len(order), 2):
    pay += menu[order[i] + 1] * order[i + 1]

print(f'총 금액은 {pay}원입니다.')
q = int(input('금액을 입력하세요. >> '))

if q >= pay:
    print('\n주문이 완료되었습니다.\n===========================')
    for i in range(0, len(order), 2):
        print(f'{menu[order[i]]}      {order[i + 1]}개')
        
    print(f'\n\n총 금액 : {pay}원\n잔액 : {q - pay}원\n===========================\n감사합니다.')
    
else:
    print('\n===========================\n금액이 부족하여 주문이 취소되었습니다.\n감사합니다.')
