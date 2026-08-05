class Animal:
    def __init__(self, species, age, name):
        self.species = species
        self.age = age
        self.name = name

    def eat(self):
        print(f'{self.name} 이(가) 먹이를 먹습니다.')


    def move(self):
        print(f'{self.name} 이(가) 움직입니다.')
        

    def make_sound(self):
        print(f'{self.name} 이(가) 소리를 냅니다.')


class Dog(Animal):
    def bark(self): # 메소드 추가
        print(f'{self.name} 이(가) 멍멍 짖습니다.')


class Cat(Animal):
    def meow(self):
        print(f'{self.name} 이(가) 야용 소리를 냅니다.')



# 객체명 = 클래스명(속성값1, 속성값2,...)
dog = Dog('개', 3, '멍멍이')
cat = Cat('고양이', 2, '야옹이')

# 객체 속성에 접근: 객체명 속성
print(dog.species)
print(dog.age)
print(dog.name)

print(cat.species)
print(cat.age)
print(cat.name)

# 객체의 메서드 접근: 객체명.메소드()
dog.eat()
dog.move()
dog.make_sound()
dog.bark()

cat.eat()
cat.move()
cat.make_sound()
cat.meow()

