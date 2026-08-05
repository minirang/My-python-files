chicken = 10 # 남은 치킨수
waiting = 1 # 대기번호


while True:
    print('남은 치킨 : ', chicken, '\n')
    try:
        order = int(input('치킨 몇 마리를 주문하시겠습니까? >> '))

        if order < 1: raise ValueError
        if chicken == 0: raise KeyError
        if order > chicken: raise TypeError
        if order > 10: raise NameError
        else:
            print('[대기번호{0}] {1}마리를 주문.'.format(waiting, order))
            waiting += 1
            chicken -= order

    except ValueError: print('정확한 값을 입력해주세요.')
    except TypeError: print('재료가 부족합니다.')
    except KeyError: print('재료가 소진되어 더 이상 주문을 받을 수 없습니다.')
    except NameError: print('한번에 10개까지만 주문이 가능합니다.')
    finally:
        print('저희 업소를 이용해 주셔서 감사합니다.\n\n')
