class Person:
    def setInfo(self, name, email):
        self.name = name
        self.email = email
    def printInfo(self):
        print(f'Name : {self.name}')
        print(f'Email : {self.email}')

member1 = Person()
member1.setInfo('Lee', 'lee@python.com')
member1.printInfo()

# 정답: member1.printInfo()