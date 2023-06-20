#! /usr/bin/env python3

import length_converter


def display_title():
    print("Feet and Meters Converter\n")


def display_menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")


def main():

    display_title()

    another_conversion = "y"

    while another_conversion.lower() == "y":
        display_menu()

        conversion = input("Select a conversion (a/b): ")

        if conversion == "a":
            feet = float(input("\nEnter feet: "))
            meters = length_converter.to_meters(feet)
            print(f"{round(meters, 2)} meters")
        elif conversion == "b":
            meters = float(input("\nEnter meters: "))
            feet = length_converter.to_feet(meters)
            print(f"{round(feet, 2)} feet")

        another_conversion = input("\nWould you like to perform "
                                   "another conversion? (y/n): ")
        print()

    print("Thanks, bye!")


if __name__ == "__main__":
    main()
