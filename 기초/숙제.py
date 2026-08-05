'''
ans1 = 2 > 1
ans2 = 3 != 3
print(ans1, ans2)
stat1 = 2 < 4 and 3 < 5
stat2 = 4 >= 6 or 5 <= 4
print(stat1, stat2)

cookie = int(input("먹은 쿠키 >>> "))
if cookie < 0:
    cookie *= -1
    #abs(cookie)
print("남은 쿠기: " + str(cookie) + "개")

num = int(input("홀짝수 판별할 숫자 입력 >>> "))
if num % 2 == 0:
    print(str(num) + "는 짝수입니다.")
else:
    print(str(num) + "는 홀수입니다.")

import random
ans = random.
num = int(input("숫자 입력 >>> "))
if num > ans:
    print("↓")
elif num < ans:
    print("↑")
else:
    print("정답! 🎉🎉")

num = int(input("수 입력 >>> "))
if num >= 1 and num <= 9:
    print("한 자리 숫자입니다.")
elif num >= 10 and num <= 99:
    print("두 자리 숫자입니다.")
else:
    print("세 자리 숫자입니다.")

score = int(input("점수 입력 >>> "))
if score == 0:
    print("당신의 성적: F")
elif score >= 77 and score < 88:
    print("당신의 성적: A0")
elif score >= 88 and score <= 100:
    print("당신의 성적: A+")
else:
    print("당신의 성적: B+")

print(15 >= 15)

age = int(input("나이를 입력하세요 >>> "))
if age >= 19:
    print("성인")
else:
    print("미성년")
'''







