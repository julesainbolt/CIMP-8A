#! /usr/bin/env python3

NUMBER_OF_QUARTERS = 4


def display_title():
    print("The Quarterly Sales Program\n")


def main():

    display_title()

    quarterly_sales = []

    total = 0.0

    for i in range(1, 5):
        sales = float(input(f"Enter sales for Q{i}: "))
        quarterly_sales.append(sales)
        total += sales

    print(f"\nTotal: \t\t\t\t{round(total, 2)}")
    print(f"Average Quarter: \t{round(total / NUMBER_OF_QUARTERS, 2)}")
    print(f"Lowest Quarter: \t{round(min(quarterly_sales), 2)}")
    print(f"Highest Quarter: \t{round(max(quarterly_sales), 2)}")


if __name__ == "__main__":
    main()
