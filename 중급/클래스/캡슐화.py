class MyClass:
    def __init__(self):
        self.public_attribute = 'public 속성'
        self.__private_attribute = 'private 속성'


    def public_method(self):
        print('public 메소드')


    def __private_method(self):
        print('private 메소드')


    def access_private_members(self):
        self.__private_method()
        print(self.__private_attribute)


math = MyClass()
math.public_method()
## math.__private_method()
math.access_private_members()
