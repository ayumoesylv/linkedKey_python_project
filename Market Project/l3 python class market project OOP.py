class fruit:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.income = 0.0

class market:
    def __init__(self):
        self.list = [fruit("banana", 4, 6), fruit("apple", 2, 0), fruit("orange", 1.5, 32), fruit("pear", 3, 15)]

    def sell_fruits(self, stock, price, income):
        if stock > 0:
            stock -= stock
            income += stock * price
            return True
        return False

    def restock_fruits(self, stock, price, income):
        if stock > 0:
            stock += stock
            income -= stock * price
            return True
        return False

    # def __str__(self):
        # return "name:" + self.name + ","\
               # " price:" + str(self.price) + ","\
               # " stock:" + str(self.stock)

    # def has_fruit(self, name, stock):
        # if self.name == name:




banana = fruit("banana", 4, 6)
apple = fruit("apple", 2, 0)
orange = fruit("orange", 1.5, 32)
pear = fruit("pear", 3, 15)

fruit_list = [banana, apple, orange, pear]

# def give_info(fruit_list):
    # print()


def manage_commands(fruit_list):
    cmd = ""
    income = 0
    fruit_count = 0

    while True:
        cmd = input("Please type a command: ")
        if cmd == "give info":
            print("info:")
            for fruit in fruit_list:
                print(fruit)

        #if cmd == "restock":
            #fruit = str(input("Please enter the fruit you want to restock: "))
            #for i in fruit_list:
                #if fruit in fruit_list:
                    #fruit = i

                    #amount = float(input("Please enter the amount of pounds you want to restock: "))
                    #fruit.restock_fruits(amount)
                    #print(fruit, "has been restocked by: ", amount)


    # print("Total revenue generated:", income, ", Total fruits sold:", fruit_count)


manage_commands(fruit_list)
