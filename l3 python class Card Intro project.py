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
    def __init__(self, name):
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







def create_players():
    player1 = Player("John")
    player2 = Player("Comp 1")

    print("")
    print("Player 1: ")
    print("")
    player1.get_cards()

    print("")
    print("Player 2: ")
    print("")
    player2.get_cards()

def create_deck():
    deck = Deck()
    deck.shuffle()

def deal_cards_to_players():
    pass

def
