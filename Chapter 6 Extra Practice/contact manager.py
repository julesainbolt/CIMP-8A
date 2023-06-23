#! /usr/bin/env python3


def display_title():
    print("The Contact Manager Program\n")


def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add  - Add a contact")
    print("del  - Delete a contact")
    print("exit - Exit program\n")


def display_contacts(contact_list):
    i = 1
    for contact in contact_list:
        print(f"{i}. {contact[0]}")
        i += 1


def view_contact(contact_list):

    while True:

        number = int(input("Number: "))

        if 0 < number <= len(contact_list):
            print(f"Name: {contact_list[number - 1][0]}")
            print(f"Email: {contact_list[number - 1][1]}")
            print(f"Phone: {contact_list[number - 1][2]}")
            break
        else:
            print("Invalid contact list number. Try again. ")


def add_contact(contact_list):

    contact = []

    contact_name = input("Name: ")
    contact.append(contact_name)

    contact_email = input("Email: ")
    contact.append(contact_email)

    contact_number = input("Phone: ")
    contact.append(contact_number)

    contact_list.append(contact)

    print(f"{contact[0]} was added.")


def delete_contact(contact_list):

    while True:

        number = int(input("Number: "))

        if 0 < number <= len(contact_list):
            contact = contact_list.pop(number - 1)
            print(f"{contact[0]} was deleted. ")
            break
        else:
            print("Invalid contact list number. Try again. ")


def main():

    display_title()

    display_menu()

    contacts = [["Guido van Rossum", "guido@guidovanrossum.com",
                 "+011 31 02 123 4567"],
                ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]

    while True:

        command = input("Command: ").lower()

        if command == "list":
            display_contacts(contacts)
        elif command == "view":
            view_contact(contacts)
        elif command == "add":
            add_contact(contacts)
        elif command == "del":
            delete_contact(contacts)
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again. ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
