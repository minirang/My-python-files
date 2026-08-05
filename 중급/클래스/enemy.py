class Enemy:
    def __init__(self, name, level, color):
        self.name = name
        self.level = level
        self.color = color


    def attack(self):
        print(f'{self.name} 공격!!')

    
    def move(slef):
        print(f'{self.name} 이동!!')



red_enemy = Enemy('레드데빌', 100, 'red')
blue_enemy = Enemy('블루데빌', 200, 'blue')


red_enemy.attack()

print(red_enemy.level)
