#! /usr/bin/env python3


def convert_miles_to_feet(miles):
    # There's 5280 feet in a mile
    return miles * 5280


def main():
    print("Hike Calculator\n")

    miles_walked = float(input("How many miles did you walk?: "))

    feet = convert_miles_to_feet(miles_walked)

    print(f"You walked {round(feet)} feet.")


if __name__ == "__main__":
    main()
