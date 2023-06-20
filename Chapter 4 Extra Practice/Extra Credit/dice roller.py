#! /usr/bin/env python3

import random

MAX = 6


def display_title():
    print("Dice Roller\n")


def roll_die():
    return random.randint(1, MAX)


def main():

    display_title()

    dice_roll = input("Roll the dice? (y/n): ")
    print()

    while dice_roll.lower() == "y":

        die1 = roll_die()
        die2 = roll_die()
        total = die1 + die2

        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        print(f"Total: {total}")

        if die1 == 1 and die2 == 1:
            print("Snake eyes!")
        elif die1 == 6 and die2 == 6:
            print("Boxcars!")

        dice_roll = input("\nRoll again? (y/n): ")
        print()

    print("Thanks, bye!")


if __name__ == "__main__":
    main()
