import random as rd
import time as ti

#두개 섞어논거
for n in range(1, 6):
    print(str(n) + '번째 번호는 ' + str(rd.randint(1,45)) + '입니다.')
    ti.sleep(1)

print()

## 카운트다운
for t in range(5, -1, -1):
    print(t)
    ti.sleep(1)
print('아무것도 없음')
