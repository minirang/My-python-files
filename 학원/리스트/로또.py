import random as rd

'''
liist = []
print('========= 로또 번호 ==========')
for n in range(0, 6):
    liist.append(rd.randint(1,45))

liist.sort()

for p in range(0, 6):
    print(f'{p + 1}번째 숫자는 {liist[p]}입니다.')

print('==============================')
'''


print('========== 설명 ==========\n\n1부터 45 사이의 숫자를 입력해주세요\n===========================\n')
count = 0
correct = 0
llist = []
lotto = []
while True:
    if count == 6:
        break

    else:
        num = int(input(f'{count + 1}번째 숫자 입력 >>> '))
        print()
        if num >= 1 and num <= 45:

            if num in llist:
                print("이미 입력한 숫자입니다. 다시 입력하세요.")
    
            else:
                count += 1
                llist.append(num)

        else:
            print('범위에 없는 숫자입니다. 다시 입력하세요.')

llist.sort()

lotto = rd.sample(range(1, 46), len(llist))

lotto.sort()

print("\n========== 로또 당첨 확인 ==========\n고객님이 선택하신 숫자는")
count = 0

for i in range(len(llist) - 1):
    print(llist[i], end = ", ")

    if i == 4:
        print(str(llist[len(llist) - 1]) + "입니다.\n\n")

print("로또 번호는")
for i in range(len(lotto) - 1):
    print(lotto[i], end = ", ")

    if i == 4:
        print(str(lotto[len(lotto) - 1]) + "였습니다.\n\n")

for i in range(len(llist)):
    if llist[i] in lotto:
        correct += 1

print(f'이 중 {correct}개의 숫자가 일치합니다.\n=====================================\n')
if correct == 0:
    print("아쉽게도 당첨되지 못했습니다")
elif correct == 6:
    print("1등입니다!! 🎉🎉")
else:
    print("어째든 당첨!")

