gender = input("male or female? >>> ")
if  gender == "male":
    height = float(input("enter height >>> "))
    weight = (height - 100) * 0.9
    print(str(height) + "cm의 표준 체중은 " + str(weight) + "kg입니다.")
else:
    height = float(input("enter height >>> "))
    weight = (height - 100) * 0.85
    print(str(height) + "cm의 표준 체중은 " + str(weight) + "kg입니다.")
print()
print("BMI :" , weight / float((height / 100) ** 2))
print()
print("검사 결과는 성인 기준입니다.")
print()
print("정확하지 않을수 있습니다.")
