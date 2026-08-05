'''
myFile = open('test.txt', 'w')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    myFile.write(data)
myFile.close()
'''

'''
myFile = open('test.txt', 'r')
while True:
    line = myFile.readline()
    if not line:
        break
    print(line)
myFile.close()
'''

'''
myFile = open('test.txt', 'r')
lines = myFile.readlines()
for line in lines:
    print(line)
    myFile.close()
'''

'''
myFile = open('test.txt', 'r')
data = myFile.read()
print(data)
myFile.close()
'''

'''
myFile = open('test.txt', 'r')
line = myFile.readlines()
print(line)
myFile.close()
'''

'''
myFile = open('test.txt', 'a')
for i in range(11, 21):
    data = '%d번째 줄입니다.\n' % i
    myFile.write(data)
myFile.close()
'''

'''
with open('test2.txt', 'w') as myFile:
    myFile.write('test중')
'''

