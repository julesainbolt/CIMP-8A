#! /usr/bin/env python3

import db


def display_title():
    print("Customer Data Importer\n")


def main():

    display_title()

    db.connect()

    print(f"CSV file: \t{db.CSV_FILENAME[:13]}")
    print(f"DB file:  \t{db.DB_FILENAME}")
    print(f"Table name: Customer\n")

    db.delete_all_customers()

    print("All old rows deleted from Customer table.")

    customers = db.read_csv_file()

    for customer in customers:
        db.add_customer(customer)

    print(f"{len(customers)} row(s) inserted into Customer table.")

    db.close()


if __name__ == "__main__":
    main()
