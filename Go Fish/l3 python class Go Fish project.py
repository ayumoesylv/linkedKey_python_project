# import the random package
import random


# create a class card to distinguish between ranks and suits of cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        suits = {1: "Spades", 2: "Clubs", 3: "Diamonds", 4: "Hearts"}
        return str(suits[self.suit]) + str(self.rank)


# Create a deck class to create the 52 cards set to distribute and use
class Deck:
    def __init__(self):

        self.deck = []
        for n in range(1, 5):
            for i in range(1, 14):
                obj = Card(n, i)
                self.deck.append(obj)

    def get_card(self):
        for i in self.deck:
            print(i)

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal_cards(self):
        chosen = random.choice(self.deck)
        self.deck.remove(chosen)
        return chosen


# Create the player class to hand out cards to
class Player:
    def __init__(self, name, deck):
        self.name = name
        self.cards = []
        for i in range(0, 7):
            chosen = deck.deal_cards()
            self.cards.append(chosen)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cards(self):
        for i in range(0, len(self.cards)):
            print(self.cards[i])

    def sort_player_cards(self):
        self.cards.sort(key=lambda card: card.get_rank)

    def place_pairs(self):
        pass

    def pick_one_card(self):
        pass

    def make_a_pair(self):
        pass


# Create the Go-Fish game class to play the game

# pseudo code:
# Create # of players (hardcode or input)
# Create a deck of cards, shuffle cards
# Deal 7 cards for every player
# Randomly pick a player to start play game
# Play game
# -> find all pairs and put on table (create a list to put pairs, save # of pairs)
# -> ask current player to pick a card and ask for matching a pair
# -> check the current player has no cards in hand, game over
# -> take turns to next player if applicable
# -> check who is the winner
class GoFishGame:
    def __init__(self, pcount):
        pass
        self.deck = Deck()
        self.players_count = pcount
        self.players = []
        for i in range(0, pcount):
            print("Is player", i, "a computer or human player?")
            answer = str(input("Type c for computer and h for human"))
            if answer != "c":
                pass

        # self.result = result
        # self.currentindex = 0
        # self.cardsCount = 0

    def get_player_count(self):
        return self.players_count

    def shuffle_cards(self):
        print("Before shuffle: ")
        print("--------------------")
        self.deck.get_card()

        print("After shuffle: ")
        print("--------------------")
        self.deck.shuffle()
        self.deck.get_card()

    def pick_starting_player(self):
        pass

    def find_pairs_of_cards(self):
        pass

    def


GoFish = GoFishGame(4)


# deck = Deck()

# Deck shuffling


# Players
player1 = Player("John", GoFish.deck)
player2 = Player("Anna", GoFish.deck)
player3 = Player("Betty", GoFish.deck)
player4 = Player("Arnold", GoFish.deck)

print("")
print("Player 1: ")
print("")
player1.get_cards()

print("")
print("Player 2: ")
print("")
player2.get_cards()

print("")
print("Player 3: ")
print("")
player3.get_cards()

print("")
print("Player 4: ")
print("")
player4.get_cards()

def play_go_fish():
    GoFish.shuffle_cards()
    pcount = 4
    GoFish.players_count(pcount)
    GoFish.get_player_count()
    # GoFish.

# c2

