contact = {}

def addContact(name, pn):
    contact[name] = pn
    print(f'{name}님이 등록되었습니다.')


def delContact(name):
    number = contact.get(name)
    if number == None:
        print(f'\n{name}님은 등록되어 있지 않습니다.')

    else:
        del contact[name]
        print(f'{name}님이 연락처에서 삭제되었습니다.')


def search(name):
    number = contact.get(name)
    if number == None:
        print(f'\n{name}님은 등록되어 있지 않습니다.')

    else:
        print(f'\n연락처 : {contact.get(name)}')


print('스마트폰 연력처 프로그램 ==========================\n\n메뉴 : 1. 추가   2. 검색   3. 삭제   4. 종료')

while True:
    q = int(input('\n\n선택 >>> '))

    if q == 1:
        addContact(input('이름 : '), input('전화번호 : '))

    elif q == 2:
        search(input('이름 : '))


    elif q == 3:
        delContact(input('이름 : '))

    elif q == 4:
        break

    else:
        print(f'{q}번은 메뉴는 없는 메뉴입니다.  1. 추가   2. 검색   3. 삭제   4. 종료')

print('프로그램이 종료되었습니다 ==========================')
