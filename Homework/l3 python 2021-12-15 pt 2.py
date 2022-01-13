from Queue import Queue
# question 30
# Input a sequence of transactions of form "buy x shares at $y each"
# Output total capital gain or loss for entire sequence


Shares_price = Queue()
Shares_amount = Queue()



def process_command():
    inp = input("Type command: ")
    if inp == 'buy':
        x = int(input("how many shares: "))
        y = int(input("How much it costs: "))
        Shares_price.en_queue(y)
        Shares_amount.en_queue(x)

    if inp == 'sell':
        x = int(input("how many shares: "))
        y = int(input("How much it costs: "))
        Shares_price.en_queue(y)
        Shares_amount.en_queue(x)

# put a tuple as an element to put it in one queue or make a share class

