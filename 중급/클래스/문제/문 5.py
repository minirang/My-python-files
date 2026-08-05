class Calc:
    def __init__(self, price, sale):
        self.price = price
        self.sale = sale


    def printFinalPrice(self):
        print(f'최종 가격 : {self.price - (self.price * self.sale / 100)}원')


thing = Calc(int(input('원가 입력 >> ')), int(input('할인률(%) 입력 >> ')))
thing.printFinalPrice()
