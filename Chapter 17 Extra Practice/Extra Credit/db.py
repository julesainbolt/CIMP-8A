import sqlite3
from contextlib import closing

import csv

from customer import Customer

DB_FILENAME = "customers.sqlite"
CSV_FILENAME = "customers.csv.xls"


conn = None


def connect():
    global conn
    if not conn:
        conn = sqlite3.connect(DB_FILENAME)


def close():
    if conn:
        conn.close()


def delete_all_customers():
    with closing(conn.cursor()) as c:
        sql_delete = '''DELETE FROM Customer'''
        c.execute(sql_delete)
        conn.commit()


def make_customer(row):
    return Customer(first_name=row[0], last_name=row[1], company_name=row[2],
                    address=row[3], city=row[4], state=row[5], zip_code=row[6])


def read_csv_file():

    customers = []

    with open(CSV_FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            customers.append(make_customer(row))

    customers.pop(0)

    return customers


def add_customer(customer):
    with closing(conn.cursor()) as c:
        sql_insert = '''INSERT INTO Customer (firstName, lastName, 
                        companyName, address, city, state, zip)
                        VALUES (?, ?, ?, ?, ?, ?, ?)'''
        c.execute(sql_insert, (customer.first_name, customer.last_name,
                               customer.company_name, customer.address,
                               customer.city, customer.state, customer.zip_code))
        conn.commit()

