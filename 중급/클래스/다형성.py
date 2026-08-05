class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} 이(가) 먹이를 먹습니다.')


    def move(self):
        print(f'{self.name} 이(가) 움직입니다.')
        

    def make_sound(self):
        print(f'{self.name} 이(가) 소리를 냅니다.')


class Dog(Animal):
    # 오버라이딩 예시
    def make_sound(self):
        print(f'{self.name} 이(가) 멍멍 소리를 냅니다.')


    # 오버로딩 예시
    def play(self, toy):
        if isinstance(toy, str):
            print(f'{self.name} 이(가) {toy}로 놀고 있습니다')
        else:
            print(f'{self.name} 이(가) 놀고 있습니다.')


class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} 이(가) 야용 소리를 냅니다.')



dog = Dog('멍멍이', 3)
cat = Cat('야용이', 2)

dog.eat()
dog.move()
dog.make_sound() # 오버라이딩 된 메소드 호출
dog.play('뽀로로 인형') # 오버로딩 된 메소드 호출 (문자열 인자 사용)
dog.play(123) # 오버로딩 된 메소드 호출 (정수 인자 사용)

cat.eat()
cat.move()
cat.make_sound() # 오버라이딩 된 메소드 호출
