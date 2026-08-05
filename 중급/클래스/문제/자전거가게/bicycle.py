class Bicycle:
    def __init__(self, c, p, n, q):
        self.color = c
        self.price = p
        self.name = n
        self.quantity = q
        self.assembled = 0


    def assemble(self):
        self.assembled = 1


    def repaint(self, c):
        self.color = c


    def __str__(self):
        print(f'\n자전거 정보\n  · 자전거 색깔: {self.color}색\n  · 자전거 가격: {self.price}원\n  · 자전거 이름: {self.name}\n  · 수량: {self.quantity}개\n')
