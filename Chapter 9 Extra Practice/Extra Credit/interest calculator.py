#! /usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP

import locale as lc


def display_title():
    print("Interest Calculator\n")


def get_loan_amount():
    return Decimal(input("Enter loan amount:    "))


def get_interest_rate():
    return Decimal(input("Enter interest rate:  "))


def calculate_interest_amount(loan_amount, interest_rate):
    return loan_amount * (interest_rate / 100)


def main():

    result = lc.setlocale(lc.LC_ALL, "")

    if result[0] == "C":
        lc.setlocale(lc.LC_ALL, "en_US")

    display_title()

    continue_program = "y"
    while continue_program.lower() == "y":

        # User input
        loan_amount = get_loan_amount()
        loan_amount = loan_amount.quantize(Decimal("1.00"), ROUND_HALF_UP)

        interest_rate = get_interest_rate()
        interest_rate = interest_rate.quantize(Decimal("1.000"), ROUND_HALF_UP)

        # Calculate interest amount

        interest_amount = calculate_interest_amount(loan_amount, interest_rate)
        interest_amount = interest_amount.quantize(Decimal("1.00"), ROUND_HALF_UP)

        # Display loan amount

        print("\nLoan amount:\t\t  {:>12}".format(lc.currency(loan_amount, grouping=True)))

        # Display interest rate

        print("Interest rate: \t\t {:>12}%".format(interest_rate))

        # Display interest amount

        print("Interest amount:\t  {:>12}".format(lc.currency(interest_amount, grouping=True)))

        continue_program = input("\nContinue? (y/n): ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
