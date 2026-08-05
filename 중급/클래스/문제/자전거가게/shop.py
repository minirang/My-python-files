class Shop:
    stock, revenue = [], 0
    
    def __init__(self):
        pass


    def sell(self, index, quantity):
        name = self.stock[index][0]
        price = self.stock[index][1]
        left_quantity = self.stock[index][2]
        self.revenue += price * quantity
        if quantity > left_quantity:
            print('입력한 수량이 남은 수량보다 많습니다.\n')

        elif left_quantity == 1:
            self.stock.pop(index)
            print(f'팔림: {name}, (1개)\n')

        else:
            self.stock[index][2] -= quantity
            print(f'팔림: {name}, ({quantity}개)\n')


    def add(self, n, p, q):
        b = [n, p, q]
        self.stock.append(b)


    def list_stock(self, show):
        if show == True:
            print('\n========= 재고 =========')
            if self.stock == []:
                print('비어있음')
                print('========================\n')
                return 'empty'

            else:
                for item in self.stock:
                    print(f'{item[0]}, {item[1]}원, {item[2]}개')

            print('========================\n')
        else:
            if self.stock == []:
                return 'empty'

            else:
                pass


    def print_revenue(self):
        print(f'매출: {self.revenue}원\n')
