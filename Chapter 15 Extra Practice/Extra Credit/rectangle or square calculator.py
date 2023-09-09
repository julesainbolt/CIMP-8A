#! /usr/bin/env python3

from rectangle import Rectangle, Square


def display_title():
    print("Rectangle Calculator\n")


def get_height():
    return int(input("Height: \t"))


def get_width():
    return int(input("Width: \t\t"))


def get_length():
    return int(input("Length: \t"))


def main():

    display_title()

    continue_program = "y"
    while continue_program.lower() == "y":

        choice = input("Rectangle or square? (r/s): ").lower()

        if choice == "r":
            rectangle = Rectangle(get_height(), get_width())

            print(f"Perimeter:  {rectangle.calculate_perimeter()}")
            print(f"Area: \t\t{rectangle.calculate_area()}")

            print(rectangle)

        elif choice == "s":
            square = Square(get_length())

            print(f"Perimeter:  {square.calculate_perimeter()}")
            print(f"Area: \t\t{square.calculate_area()}")

            print(square)

        continue_program = input("\nContinue? (y/n): ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
