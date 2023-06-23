#! /usr/bin/env python3


def display_title():
    print("The Wizard Inventory Program\n")


def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program\n")


def show_items(inventory_list):
    i = 1
    for item in inventory_list:
        print(f"{i}. {item}")
        i += 1


def grab_item(inventory_list):

    if len(inventory_list) == 4:
        print("You can't carry any more items. Drop something first. ")
    else:
        item = input("Name: ")
        inventory_list.append(item)
        print(f"{item} was added.")


def edit_item(inventory_list):

    while True:

        item_number = int(input("Number: "))

        if 0 < item_number <= len(inventory_list):
            updated_name = input("Updated name: ")
            inventory_list[item_number - 1] = updated_name
            print(f"Item number {item_number} was updated. ")
            break
        else:
            print("Invalid item number. Try again. ")


def drop_item(inventory_list):

    while True:

        item_number = int(input("Number: "))

        if 0 < item_number <= len(inventory_list):
            print(f"{inventory_list.pop(item_number - 1)} was dropped. ")
            break
        else:
            print("Invalid item number. Try again. ")


def main():

    display_title()

    display_menu()

    inventory = ["wooden staff", "wizard hat", "cloth shoes"]

    while True:

        command = input("Command: ").lower()

        if command == "show":
            show_items(inventory)
        elif command == "grab":
            grab_item(inventory)
        elif command == "edit":
            edit_item(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again. ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
