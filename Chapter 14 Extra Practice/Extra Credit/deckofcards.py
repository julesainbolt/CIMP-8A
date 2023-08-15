
import random


class Card:
    def __init__(self, rank="", suit=""):
        self.rank = rank
        self.suit = suit

    def get_string_depiction(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
                      "Queen", "King", "Ace"]
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def count_cards_in_deck(self):
        return len(self.cards)

    def deal_card(self):
        card = random.choice(self.cards)
        index = self.cards.index(card)
        return self.cards.pop(index)
