#! /usr/bin/env python3

print("=" * 63)
print("Shipping Calculator")
print("=" * 63)

continue_program = "y"
while continue_program.lower() == "y":
    # User input
    cost_of_items = float(input("Cost of items ordered: "))
    shipping_cost = 0.0

    if cost_of_items < 0.0:
        print("You must enter a positive number. Please try again. ")
        continue
    elif cost_of_items < 30.00:
        shipping_cost = 5.95
    elif 30.00 <= cost_of_items <= 49.99:
        shipping_cost = 7.95
    elif 50.00 <= cost_of_items <= 74.99:
        shipping_cost = 9.95
    elif cost_of_items == 75.00:
        shipping_cost = 0.0

    # Display shipping cost
    print(f"Shipping cost: \t\t   {shipping_cost}")

    # Calculate and display total cost
    total_cost = round(cost_of_items + shipping_cost, 2)
    print(f"Total cost: \t\t   {total_cost}")

    continue_program = input("\nContinue? (y/n): ")
    print("=" * 63)

print("Bye!")
