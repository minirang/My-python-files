'''
fee = 25000
age = int(input("나이 입력 >>> "))

if age > 0 and age < 8:
    print("입장료 무료")
elif age >= 8 and age < 60:
    print("입장료: ", fee, "원")
else:
    print("입장료: ", fee * 0.5, "원")
exit

fee = 25000
age = int(input("나이 입력 >>> "))

if age > 0 and age < 8:
    print("입장료 무료")
elif age >= 8 and age < 60:
    print("입장료: ", fee, "원")
elif age >= 60:
    print("입장료: ", fee * 0.5, "원")
else:
    print("나이 오류")
'''


'''
inputpw == pw and inputuid == uid  다 맞음
inputpw == pw and inputuid == uid else  다 틀림
inputuid == uid else  uid만 틀림
inputpw == pw else  pw만 틀림

uid = "minirang"
pw = "pw"

inputuid = input("아이디 입력 >>> ")
inputpw = input("비밀번호 입력 >>> ")

if inputuid == uid:
    if inputpw == pw:
        print("로그인 성공")
    else:
        print("비번 불일치")
else:
    print("아이디 불일치")

print(not True)

num = int(input("정수 입력 >>> "))
if num % 2 == 0:
    print(str(num) + "은/는 짝수")
else:
    print(str(num) + "은/는 홀수")

score = int(input("점수 입력 >>> "))

if score >= 90:
    print(str(score) + "점은 A학점")
elif score >= 80 and score < 90:
    print(str(score) + "점은 B학점")
elif score >= 70 and score < 80:
    print(str(score) + "점은 C학점")
elif score >= 60 and score < 70:
    print(str(score) + "점은 D학점")
elif score < 60:
    print(str(score) + "점은 F학점")


height = int(input("키 입력 (cm) >>> "))
weight = int(input("몸무게 입력 (kg) >>> "))

if height >= 120 and weight >= 40:
    print("바이킹 탑승 가능")
else:
    print("바이킹 탑승 불가능")
'''
