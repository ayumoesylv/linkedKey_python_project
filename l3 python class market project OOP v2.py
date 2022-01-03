class fruit:
    def __init__(self, name, price, stock, income):
        self.name = name
        self.price = price
        self.stock = stock
        self.income = income

    def info(self, list):
        for i in list:
            print(i.name)
            print(i.price)
            print(i.stock)

    def sell(self, stock, price, income):
        if stock > 0:
            stock -= stock
            income += stock * price
            return True
        return False

    def restock(self, stock, price, income):
        if stock > 0:
            stock += stock
            income -= stock * price
            return True
        return False

# operations to take on fruit

class market:
    def __init__(self, list):
        self.list = list

    def give_info(self):



# class not necessary
class discount:
    def __init__(self, discount):
        self.discount = discount

    def reduce(self, price, discount):
        price = discount*price
        return price


banana = fruit("banana", 4, 6, 0.0)
apple = fruit("apple", 2, 0, 0.0)
orange = fruit("orange", 1.5, 32, 0.0)
pear = fruit("pear", 3, 15, 0.0)
fruit_list = [banana, apple, orange, pear]


def manage_commands():
    cmd = ""
    income = 0
    fruit_count = 0
    m = market(fruit_list)

    while True:
        cmd = input("Please type a command: ")
        if cmd == "give info":
            print("info:")

            m.info(fruit_list)

        if cmd == "restock":
            fruit_req = str(input("Please enter the fruit you want to restock: "))
            for i in fruit_list:
                if fruit_req == i.name:
                    # print(i.name)
                    stock_req = float(input("Plese enter the pounds you want to restock: "))
                    m.restock(stock_req, i.price, income)
                    print(i.income)

        if cmd == "buy":
            fruit_req = str(input("Please enter the fruit you want to buy: "))
            for i in fruit_list:
                if fruit_req == i.name:
                    stock_req = float(input("Please enter the pounds you want to buy: "))
                    m.sell(stock_req, i.price, income)


            # restock



    # print("Total revenue generated:", income, ", Total fruits sold:", fruit_count)


manage_commands()
