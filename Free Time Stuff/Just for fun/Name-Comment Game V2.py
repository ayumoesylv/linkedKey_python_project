import random

the_stinky_dictionary = {1: "ran away to Alberta.", 2: "is good at math.", 3: "is an amazing person.",
                         4: "should give me 100 dollars right now.", 5: "fell down the stairs.",
                         6: "threw up projectile vomit.", 7: "is going to be sacrificed to the blood god on Tuesday.",
                         8: "is a vampire.", 9: "is going to be a billionaire.", 10: "owes me skittles.", 11: "has a secret crush on the previous person.", 12: "needs to take a shower."}


def play_random_comment():
    print("If you want to quit, type q in the input name prompt.")
    to_name = ""
    while to_name != "q":

        from_name = input("")
        print("is thinking...")
        to_name = input(" ")
        if to_name == "q":
            break

        rand = random.randint(1, 12)

        print(the_stinky_dictionary[rand])


play_random_comment()
