'''
print('나누기 계산기입니다.')

try:
    num1=int(input('첫번째 수 입력 >> '))
    num2=int(input('두번째 수 입력 >> '))
    print(f'{num1}/{num2}={num1/num2}')

#try문 후 except 오류명
except ValueError:
    print('잘못된 값 입력')
except ZeroDivisionError as err:
    print(err)
'''

## 입력받는 수가 한자리가 아닌 경우 에러 발생 후 오류와 상관없이 마지막 메시지 실행하기
print('나누기 계산기입니다.')

try:
    num1=int(input('첫번째 수 입력 >> '))
    num2=int(input('두번째 수 입력 >> '))
    if num1 >= 10 or num2 >= 10:
        raise ValueError

    print(f'{num1}/{num2} = {num1/num2}')

#try문 후 except 오류명
except ValueError:
    print('잘못된 값 입력')
except ZeroDivisionError as err:
    print(err)
finally: # 오류와 상관없이 실행
    print('계산기를 이용해 주셔서 감사합니다.')
