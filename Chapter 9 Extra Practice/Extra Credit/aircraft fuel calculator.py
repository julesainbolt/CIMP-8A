#! /usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP

MINUTES_IN_HOUR = 60

NAUTICAL_MILES_PER_HOUR = 120
GALLONS_OF_GAS_PER_HOUR = 8.4


def display_title():
    print("Aircraft Fuel Calculator\n")


def get_nautical_miles():
    return Decimal(input("Distance in nautical miles: "))


def calculate_flight_time(nautical_miles):
    hr = nautical_miles / NAUTICAL_MILES_PER_HOUR

    # Convert hours to minutes
    min = hr * MINUTES_IN_HOUR

    # Use integer division to extract hours
    hours = min // MINUTES_IN_HOUR

    # Use mod operator to extract remaining minutes
    minutes = round(min % MINUTES_IN_HOUR)

    return hours, minutes


def calculate_required_fuel(nautical_miles):
    gallons = Decimal("0.0")
    gallons = ((nautical_miles / NAUTICAL_MILES_PER_HOUR) + Decimal("0.5")) * Decimal(GALLONS_OF_GAS_PER_HOUR)
    gallons = gallons.quantize(Decimal("1.0"), ROUND_HALF_UP)
    return gallons


def main():

    display_title()

    continue_program = "y"
    while continue_program.lower() == "y":

        # User input
        nautical_miles = get_nautical_miles()

        # Calculate and display flight time

        hours, minutes = calculate_flight_time(nautical_miles)

        print(f"Flight time: {hours} hour(s) and {minutes} minute(s)")

        # Calculate and display required fuel

        gallons = calculate_required_fuel(nautical_miles)

        print(f"Required fuel: {gallons} gallons")

        continue_program = input("\nContinue? (y/n): ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
