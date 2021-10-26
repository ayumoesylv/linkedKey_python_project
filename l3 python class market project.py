# 13 a. Initially, create a dictionary called prices
# to record the price (dollars/lb) for each fruit.
# Put these values in the prices dictionary:

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# 13 b. Initially, create a dictionary called stock
# to record the weight (pound) for each fruit.
# Put these values in the stock dictionary:

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

# 13 c. Print out the top two fruits with higher prices.

def determine_highest_prices(price: dict):
    key_of_max = ""
    maximum = 0

    for key in price:
        value = price[key]
        if value > maximum:
            maximum = value
            key_of_max = key

    return maximum, key_of_max


def get_specified_top(price: dict, numsort):
    highest_prices = {}
    new_price = price.copy()
    for i in range(0, numsort):
        mn, key = determine_highest_prices(new_price)
        high_price = {key : mn}
        highest_prices.update(high_price)

        new_price.pop(key)

    return highest_prices

# rf - request fruit, rs - request stock, hs - have stock
def buy(price: dict, stock: dict):
    rf = str(input("Please order your fruit: "))
    rs = float(input("Please order your stock: "))

    if rf not in stock:
        print("not available.")
        return

    hs = stock[rf]

    if hs < rs:
        print(rf, "must be restocked.")

    else:
        hs = hs - rs
        print("Sold", rs, "pounds of", rf, "Total: ", rs * price[rf])

    stock[rf] = hs
    return rf, rs

# rsf - restock fruit, rss - restock stock
def restock(price: dict, stock: dict):
    rsf = str(input("Please type fruit to be restocked: "))
    rss = float(input("Please type restock amount: "))

    if rsf not in stock:
        print("not available.")
        # handle special value with none, none
        return

    stock[rsf] += rss
    print("Restocked", rss, "pounds of", rsf, ". Expense: ", rss * price[rsf])
    # return rss
    return rsf, rss



def manage_commands(price, stock):
    cmd = ""
    income = 0
    fruit_count = 0

    while True:
        cmd = input("Please type a command: ")
        if cmd == "give info":
            print("Prices: ", prices, "Stock: ", stock, "Top prices", get_specified_top(prices, 2))

        if cmd == "buy":
            fruit, pound = buy(prices, stock)
            income += (prices[fruit]*pound)
            fruit_count += pound

        if cmd == "restock":
            fruit, pound = restock(prices, stock)
            income -= (prices[fruit]*pound)

        if cmd == "dayend":
            print("Thank you for shopping!")
            break

    print("Total revenue generated:", income, ", Total fruits sold:", fruit_count)


manage_commands(prices, stock)

#c2
