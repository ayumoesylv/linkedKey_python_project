class fruit:
    def __init__(self, name, price, stock, income):
        self.name = name
        self.price = price
        self.stock = stock
        self.income = income

    # def info(self, list):
        # return self.name, self.price, self.stock

    def sell(self, stock, price, income):
        if self.stock > 0:
            self.stock -= stock
            self.income += stock * price
            return True
        return False

    def restock(self, stock, price, income):
        self.stock += stock
        self.income -= stock * price


# operations to take on fruit

class market:
    def __init__(self, list):
        self.list = list

    def get_fruit(self, list, specf):
        for i in list:
            if i.name == specf:
                return i
        return 0

    def give_info(self):
        for i in fruit_list:
            print(i.name, i.price, i.stock, i.income)

    def list_top_two(self, list):
        prices = [(fruit.price, fruit.name) for fruit in list]
        sorted_prices = sorted(prices, reverse=True)
        for i in range(0, 2):
            print(sorted_prices[i])

    def sell_fruit(self, specf, specs):
        f = self.get_fruit(fruit_list, specf)
        sell = f.sell(specs, f.price, f.income)
        if sell:
            print("Sold", specs, "pounds of", specf)
            print("Current stock: ", f.stock)
            print("Current income for",specf, ": ", f.income)
        else:
            print(specf, "needs to be restocked.")
        # print(f.stock, f.income)

    def restock_fruit(self, specf, specs):
        f = self.get_fruit(fruit_list, specf)
        if f == 0:
            specp = int(input("Please enter price to set: "))
            income = specs * specp
            fruit_list.append(fruit(specf, specp, specs, 0.0 - income))
            print("Added", specf, "to market. Restocked", specs, "pounds of", specf)

        else:
            f.restock(specs, f.price, f.income)
            print("Restocked", specs, "pounds of", specf)
            print("Current stock: ", f.stock)
            print("Current income for",specf, ": ", f.income)


banana = fruit("banana", 4, 6, 0.0)
apple = fruit("apple", 2, 0, 0.0)
orange = fruit("orange", 1.5, 32, 0.0)
pear = fruit("pear", 3, 15, 0.0)
fruit_list = [banana, apple, orange, pear]


def manage_commands():
    cmd = ""
    m = market(fruit_list)

    while True:
        cmd = input("Please type a command: ")
        if cmd == "give info":
            m.give_info()

        if cmd == "top prices":
            m.list_top_two(fruit_list)

        if cmd == "buy":
            fruit_req = str(input("Please enter the fruit you want to buy: "))
            stock_req = int(input("Please request the stock: "))
            m.sell_fruit(fruit_req, stock_req)

        if cmd == "restock":
            fruit_req = str(input("Please enter the fruit you want to restock: "))
            stock_req = int(input("Plese enter the pounds you want to restock: "))
            m.restock_fruit(fruit_req, stock_req)

        if cmd == "dayend":
            total = 0.0
            for i in fruit_list:
                print(i.name, ": $", i.income)
                total += i.income
            print("Total income: $", total)
            break





    # print("Total revenue generated:", income, ", Total fruits sold:", fruit_count)


manage_commands()
