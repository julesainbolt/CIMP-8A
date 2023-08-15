#! /usr/bin/env python3

from deckofcards import Deck


def display_title():
    print("Card Dealer\n")


def main():

    display_title()

    deck = Deck()

    deck.shuffle_deck()

    print(f"I have shuffled a deck of {deck.count_cards_in_deck()} cards.\n")

    number_of_cards = int(input("How many cards would you like?: "))

    print("\nHere are your cards: ")

    for i in range(number_of_cards):
        card = deck.deal_card()
        print(card.get_string_depiction())

    print(f"\nThere are {deck.count_cards_in_deck()} cards left in the deck.\n")

    print("Good luck!")


if __name__ == "__main__":
    main()
