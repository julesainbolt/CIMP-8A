#! /usr/bin/env python3

import csv

FILENAME = "monthly_sales.csv.xls"

MONTHS = 12


def display_title():
    print("The Monthly Sales Program\n")


def display_menu():
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("yearly  - View yearly summary")
    print("edit    - Edit sales for a month")
    print("exit    - Exit program\n")


def write_sales(sales_list):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales_list)


def read_sales():
    sales = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append(row)
    return sales


def display_monthly_sales(sales_list):
    for sale in sales_list:
        print(f"{sale[0]} - {sale[1]}")


def display_yearly_summary(sales_list):

    total = 0
    for sale in sales_list:
        total += int(sale[1])

    print(f"Yearly total: \t  {total}")
    print(f"Monthly average:  {round(total / MONTHS, 2)}")


def edit_monthly_sales(sales_list):

    while True:

        month = input("Three-letter Month: ").lower()
        sales_amount = input("Sales Amount: ")

        for sale in sales_list:
            if month == sale[0].lower():
                sale[1] = sales_amount
                write_sales(sales_list)
                print(f"Sales amount for {month} was modified. ")
                return

        print("Invalid three-letter month. Try again. ")


def main():

    display_title()

    display_menu()

    sales = read_sales()

    while True:

        command = input("Command: ").lower()

        if command == "monthly":
            display_monthly_sales(sales)
        elif command == "yearly":
            display_yearly_summary(sales)
        elif command == "edit":
            edit_monthly_sales(sales)
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again. ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
