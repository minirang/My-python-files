'''
## 추가하기
cart = []
order = 0

while True:
    thing = input("장바구니에 담을 물건 선택 >>> ") #우유
    n = int(input("수량 >>> ")) #5

    cart.append(thing)
    cart.append(n)

    print(f"고객님의 장바구니에 {cart[-2]} {n}개가 저장되었습니다.") #["우유", 5]

    order = input("추가주문을 하시겠습니까? 예 / 아니요 >>> ")
    if order == "아니요":
        break

print("\n====== 고객님의 장바구니 ======")

num = 1

for i in range(0, len(cart), 2):
    print(str(num) + '. ' + cart[i] + '    ' + str(cart[i + 1]) + '개')
    num += 1
print('===============================')

## 삭제하기
cart = ['우유', 3, '바나나', 2, '새우깡', 1]
thing = input('삭제할 물품 입력 >>> ')
if thing in cart:
    del(cart[cart.index(thing) + 1])
    cart.remove(thing)
    
    print("\n====== 고객님의 장바구니 ======")
    num = 1

    for i in range(0, len(cart), 2):
        print(str(num) + '. ' + cart[i] + '    ' + str(cart[i + 1]) + '개')
        num += 1
    print('===============================')
else:
    print('카트에는 그런 물건 없어요')


## 수정하기
cart = ['우유', 3, '바나나', 2, '새우깡', 1]
thing = input('수정할 물품 입력 >>> ')
if thing in cart:
    n = int(input(f'{thing}의 새로운 수량 입력 >>> '))
    cart[cart.index(thing) + 1] = n

    print("\n====== 고객님의 장바구니 ======")
    num = 1

    for i in range(0, len(cart), 2):
        print(str(num) + '. ' + cart[i] + '    ' + str(cart[i + 1]) + '개')
        num += 1
    print('===============================')
else:
    print('카트에는 그런 물건 없어요')
'''
    






