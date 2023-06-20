#! /usr/bin/env python3


def display_title():
    print("Even or Odd Checker\n")


def check_even_or_odd(number):
    return number % 2


def main():

    display_title()

    integer = int(input("Enter an integer: "))

    if check_even_or_odd(integer) > 0:
        print("This is an odd number. ")
    else:
        print("This is an even number. ")


if __name__ == "__main__":
    main()
