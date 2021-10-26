import random

the_stinky_dictionary = {1: "ran away to Alberta.", 2: "is good at math.", 3: "is an amazing person.",
                         4: "should give me 100 dollars right now.", 5: "fell down the stairs.",
                         6: "threw up projectile vomit.", 7: "is going to be sacrificed to the blood god on Tuesday.",
                         8: "is a vampire.", 9: "is going to be a billionaire.", 10: "owes me skittles."}


def play_random_comment():
    print("If you want to quit, type q in the input name prompt.")
    name = ""
    while name != "q":

        name = input("Please input your name: ")
        if name == "q":
            break

        rand = random.randint(1, 10)

        print(name, the_stinky_dictionary[rand])


play_random_comment()
