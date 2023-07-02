#! /usr/bin/env python3


def display_title():
    print("Tip Calculator\n")


def get_meal_cost():
    while True:

        try:

            meal_cost = float(input("Cost of meal: "))

        except ValueError:
            print("Must be a valid decimal number. Please try again. ")
            continue

        if meal_cost <= 0:
            print("Must be greater than 0. Please try again. ")
        else:
            return meal_cost


def get_tip_percent():
    while True:

        try:

            tip_percentage = int(input("Tip percent:  "))

        except ValueError:
            print("Must be a valid integer. Please try again. ")
            continue

        if tip_percentage <= 0:
            print("Must be greater than 0. Please try again. ")
        else:
            return tip_percentage


def calculate_tip_amount(meal_cost, tip_percent):
    return meal_cost * (tip_percent / 100)


def calculate_total_amount(meal_cost, tip_amount):
    return meal_cost + tip_amount


def main():

    display_title()

    print("INPUT")

    meal_cost = get_meal_cost()

    tip_percent = get_tip_percent()

    print("\nOUTPUT")
    print(f"Cost of meal: {meal_cost}")
    print(f"Tip percent:  {tip_percent}%")

    tip_amount = calculate_tip_amount(meal_cost, tip_percent)
    print(f"Tip amount:   {round(tip_amount, 2)}")

    total_amount = calculate_total_amount(meal_cost, tip_amount)
    print(f"Total amount: {round(total_amount, 2)}")


if __name__ == "__main__":
    main()