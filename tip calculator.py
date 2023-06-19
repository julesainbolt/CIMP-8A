#! /usr/bin/env python3

print("Tip Calculator\n")

# User input
meal_cost = float(input("Cost of meal: "))
tip_percent = float(input("Tip Percent:  "))

# Calculate and display tip amount
tip_amount = meal_cost * (tip_percent / 100)
print(f"\nTip Amount:   {round(tip_amount, 2)}")

# Calculate and display total amount
total_amount = meal_cost + tip_amount
print(f"Total Amount: {round(total_amount, 2)}")
