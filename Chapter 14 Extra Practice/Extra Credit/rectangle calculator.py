#! /usr/bin/env python3

from rectangle import Rectangle


def display_title():
    print("Rectangle Calculator\n")


def get_height():
    return int(input("Height: \t"))


def get_width():
    return int(input("Width: \t\t"))


def main():

    display_title()

    continue_program = "y"
    while continue_program.lower() == "y":

        rectangle = Rectangle(get_height(), get_width())

        print(f"Perimeter:  {rectangle.calculate_perimeter()}")
        print(f"Area: \t\t{rectangle.calculate_area()}")

        rectangle.get_string_depiction()

        continue_program = input("\nContinue? (y/n): ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
