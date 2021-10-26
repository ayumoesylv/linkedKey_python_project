class fruit:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.income = 0.0

class market:
    def __init__(self):
        banana = fruit("banana", 4, 6)
        apple = fruit("apple", 2, 0)
        orange = fruit("orange", 1.5, 32)
        pear = fruit("pear", 3, 15)
        self.list = [banana, apple, orange, pear]

    def info(self):
        for i in self.list:
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




def manage_commands():
    cmd = ""
    income = 0
    fruit_count = 0
    m = market()

    while True:
        cmd = input("Please type a command: ")
        if cmd == "give info":
            print("info:")

            m.info()

        if cmd == "restock":
            fruit_req = str(input("Please enter the fruit you want to restock: "))
            if fruit_req = m.list(
            # restock



    # print("Total revenue generated:", income, ", Total fruits sold:", fruit_count)


manage_commands()
