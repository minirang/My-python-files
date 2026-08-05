class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def printInfo(self):
        print(f'Name : {self.name}')
        print(f'Email : {self.email}')


member1 = Person('Lee', 'lee@python.com')
member1.printInfo()

# 정답: __init__
