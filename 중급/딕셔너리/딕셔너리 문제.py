'''
word = {}
while True:
    q = input('단어 입력 >>> ')
    if q == "끝":
        break
    else:
        word[q] = len(q)
        
print(word)
'''

'''
num = {"홀수": [], "짝수": []}
while True:
    q = int(input('숫자 입력 >>> '))
    if q == -1:
        break
    else:
        if q % 2 == 0:
            num["짝수"].append(q)
        else:
            num["홀수"].append(q)
            
print(num)
'''

'''
def getAverage(lists):
    n = 0
    for i in range(3):
        n += lists[i]
    n /= len(lists)
    return format(n, ".1f") # 소수점 1자리까지


scores = {'홍길동': [90, 80, 95],
          '장동건': [85, 75, 90],
          '이효리': [80, 75, 90]}

print(f'홍길동 : 평균 {getAverage(scores["홍길동"])}점')
print(f'장동건 : 평균 {getAverage(scores["장동건"])}점')
print(f'이효리 : 평균 {getAverage(scores["이효리"])}점')
'''

