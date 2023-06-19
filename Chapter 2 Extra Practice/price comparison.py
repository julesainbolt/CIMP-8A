#! /usr/bin/env python3

print("Price Comparison\n")

# User input
price1 = float(input("Price of 64 oz size: "))
price2 = float(input("Price of 32 oz size: "))

# Calculate and display price per ounce
print(f"\nPrice per oz (64 oz): {round(price1 / 64, 2)}")
print(f"Price per oz (32 oz): {round(price2 / 32, 2)}")
