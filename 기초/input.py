'''
money= int(input("액수 >>>"))*2
print(money,"원")

school= input("어디 학교? >>>")
name= input("이름? >>>")
phone_num= input("연락처? >>>")
print()
print("학교 :", school)
print("이름 :", name)
print("연락처 :", phone_num)

height= int(input("키? >>>"))
weight= (height-100)*0.9
print(str(height)+"cm의 표준 체중은 "+str(weight)+"kg입니다.")

subject_num= 0
Korean_score= int(input("국어시험 점수 입력 >>>"))
subject_num += 1
English_score= int(input("영어시험 점수 입력 >>>"))
subject_num += 1
math_score= int(input("수학시험 점수 입력 >>>"))
subject_num += 1
all_score= Korean_score + English_score + math_score
avg= all_score / subject_num
print("총점 : "+ str(all_score) + "점")
print("평균 : "+ str(avg) + "점")

people= int(input("파티 참석자 수 >>>"))
cider_coke= people * 2
print("치킨 : "+str(people)+"마리")
print("사이다 : "+str(cider_coke)+"캔")
print("콜라 : "+str(cider_coke)+"캔")

money = int(input("한국돈 입력 >>> "))
dollar = money // 1200
change = money % 1200
print("환전할 달러 : " + str(dollar) + "달러")
print("남은 금액 : " + str(change) + "원")

attend = int(input("attend >>> "))
homework = int(input("homework >>> "))
mid = int(input("mid >>> "))
final = int(input("final >>> "))
all_score = attend / 100 * 10 + homework / 100 * 30 + mid / 100 * 30 + final / 100 * 30
print("총점 : " + str(all_score) + "점")

num = int(input("숫자 입력 >>> "))
hundred = num // 100
ten = int((num - num // 100 * 100 - num % 10) / 10)
one = num % 10
print("백의 자리 : " + str(hundred))
print("십의 자리 : " + str(ten))
print("일의 자리 : " + str(one))

time = int(input("시간입력(초) >>> "))
h=time // 3600
m=time % 3600 // 60
s=time % 3600 % 60
print(str(h) + "시간")
print(str(m) + "분")
print(str(s) + "초")
'''
