#! /usr/bin/env python3

print("Change Calculator")

continue_program = "y"
while continue_program.lower() == "y":
    number_of_cents = int(input("\nEnter number of cents (0-99): "))
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    result = number_of_cents // 25
    remainder = number_of_cents % 25

    if result >= 0:
        quarters = result
        result = remainder // 10
    if result >= 0:
        dimes = result
        remainder %= 10
        result = remainder // 5
    if result >= 0:
        nickels = result
        remainder %= 5
        result = remainder // 1
    if result >= 0:
        pennies = result
        remainder %= 1

    print(f"\nQuarters: {quarters}")
    print(f"Dimes: \t  {dimes}")
    print(f"Nickels:  {nickels}")
    print(f"Pennies:  {pennies}")

    continue_program = input("\nContinue? (y/n): ")

print("\nBye!")
