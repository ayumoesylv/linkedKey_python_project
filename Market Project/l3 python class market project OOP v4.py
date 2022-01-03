class fruit:
    def __init__(self, name, price, stock, income, discount):
        self.name = name
        self.price = price
        self.stock = stock
        self.income = income
        self.discount = discount

    def sell(self, stock, price, income):
        if self.stock > 0:
            self.stock -= stock
            self.income += stock * price
            return True
        return False

    def restock(self, stock, price, income):
        self.stock += stock
        self.income -= stock * price


class market:
    def __init__(self, list, name):
        self.list = list
        self.name = name

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
            print("Current income for", specf, ": ", f.income)
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
            print("Current income for", specf, ": ", f.income)


# supermarket 1
apple = fruit("apple", 2, 10, 0.0, 0)
banana = fruit("banana", 4, 10, 0.0, 0)
blueberry = fruit("blueberry", 1, 10, 0.0, 0)
cherry = fruit("cherry", 6, 10, 0.0, 0)
dragonfruit = fruit("dragonfruit", 6, 10, 0.0, 0)

# supermarket 2
grape = fruit("grape", 1, 10, 0.0, 0)
grapefruit = fruit("grapefruit", 3, 10, 0.0, 0)
kiwi = fruit("kiwi", 2, 10, 0.0, 0)
lime = fruit("lime", 2, 10, 0.0, 0)
mango = fruit("mango", 4, 10, 0.0, 0)

# supermarket 3
orange = fruit("orange", 1.5, 10, 0.0, 0)
papaya = fruit("papaya", 3, 10, 0.0, 0)
peach = fruit("peach", 3, 10, 0.0, 0)
pear = fruit("pear", 3, 10, 0.0, 0)
pomegranate = fruit("pomegranate", 5, 10, 0.0, 0)

# supermarket 4
pineapple = fruit("pineapple", 6, 10, 0.0, 0)
passionfruit = fruit("passionfruit", 6, 10, 0.0, 0)
raspberries = fruit("raspberries", 1, 10, 0.0, 0)
strawberries = fruit("strawberries", 1, 10, 0.0, 0)
watermelon = fruit("watermelon", 8, 10, 0.0, 0)

fruit_list = [apple, banana, blueberry, cherry, dragonfruit]
fruit_list2 = [grape, grapefruit, kiwi, lime, mango]
fruit_list3 = [orange, papaya, peach, pear, pomegranate]
fruit_list4 = [pineapple, passionfruit, raspberries, strawberries, watermelon]

Loblaws = market(fruit_list, "Loblaws")
NoFrills = market(fruit_list2, "NoFrills")
SunnySide = market(fruit_list3, "SunnySide")
TnT = market(fruit_list4, "TnT")


def manage_commands(m):
    cmd = ""
    print("Welcome to", m.name, "!")
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


manage_commands(Loblaws)
manage_commands(NoFrills)
manage_commands(SunnySide)
manage_commands(TnT)

# c1