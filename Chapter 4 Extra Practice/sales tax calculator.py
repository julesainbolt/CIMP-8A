#! /usr/bin/env python3

import sales_tax


def display_title():
    print("Sales Tax Calculator\n")


def main():

    display_title()

    another_calculation = "y"

    while another_calculation.lower() == "y":

        total_cost = 0.0

        print("ENTER ITEMS (ENTER 0 TO END)")

        while True:

            item_cost = float(input("Cost of item: "))

            if item_cost == 0:
                break

            total_cost += item_cost

        sale_tax = sales_tax.calculate_sales_tax(total_cost)
        total_after_tax = sales_tax.calculate_total_after_tax(total_cost, sale_tax)

        print(f"Total: \t\t\t {total_cost}")
        print(f"Sales tax: \t\t {sale_tax}")
        print(f"Total after tax: {total_after_tax}")

        another_calculation = input("\nAgain? (y/n): ")
        print()

    print("Thanks, bye!")


if __name__ == "__main__":
    main()
