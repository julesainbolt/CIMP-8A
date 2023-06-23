#! /usr/bin/env python3


def display_title():
    print("Prime Number Checker\n")


def get_int():

    while True:

        number = int(input("Please enter an integer between 1 and 5000: "))

        if 1 <= number <= 5000:
            return number
        else:
            print("Invalid number. Try again. ")


def is_prime(number):
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def add_factors(factors_list, number):
    for i in range(1, number + 1):
        if number % i == 0:
            factors_list.append(i)


def remove_factors(factors_list, number):
    index = 1
    for i in range(1, number + 1):
        if number % i == 0:
            factors_list.pop(index - 1)


def display_factors(factors_list):
    for factor in factors_list:
        print(factor, end=" ")
    print()


def main():

    display_title()

    again = "y"

    factors = []

    while again.lower() == "y":

        integer = get_int()

        add_factors(factors, integer)

        if is_prime(integer):
            print(f"{integer} is a prime number.")
        else:
            print(f"{integer} is NOT a prime number.")
            print(f"It has {len(factors)} factors:", end=" ")
            display_factors(factors)

        remove_factors(factors, integer)

        again = input("\nTry again? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
