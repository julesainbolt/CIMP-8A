#! /usr/bin/env python3

print("Registration Form\n")

first_name = input("First name: \t")
last_name = input("Last name: \t\t")
birth_year = input("Birth year: \t")

print(f"\nWelcome {first_name} {last_name}!")
print("Your registration is complete.")
print(f"Your temporary password is: {first_name}*{birth_year}")
