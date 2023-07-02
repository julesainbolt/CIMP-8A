#! /usr/bin/env python3

import random
import sys

FILENAME = "wizard_all_items.txt"


def display_title():
    print("The Wizard Inventory Program\n")


def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program\n")


def write_items(inventory_list):

    try:

        with open("wizard_current_items.txt", "w") as file:
            for item in inventory_list:
                file.write(item + "\n")
    except Exception as e:
        print(type(e), e)


def read_current_items():
    try:

        inventory = []
        with open("wizard_current_items.txt") as file:
            for line in file:
                line = line.replace("\n", "")
                inventory.append(line)
        return inventory
    except FileNotFoundError:
        print("Could not find inventory file! ")
        print("Wizard is starting with no inventory. \n")
        inventory = []
        return inventory
    except Exception as e:
        print(type(e), e)


def read_all_items():
    try:

        inventory = []
        with open(FILENAME) as file:
            for line in file:
                line = line.replace("\n", "")
                inventory.append(line)
        return inventory
    except FileNotFoundError:
        exit_program()
    except Exception as e:
        print(type(e), e)


def exit_program():
    print("Could not find items file. ")
    print("Exiting program. Bye! ")
    sys.exit()


def show_items(inventory_list):
    if len(inventory_list) == 0:
        print("There's nothing to show. ")
        return

    i = 1
    for item in inventory_list:
        print(f"{i}. {item}")
        i += 1


def grab_item(inventory_list):

    inventory = read_all_items()

    item = random.randint(1, len(inventory))

    print(f"While walking down a path, you see {inventory[item - 1]}.")

    while True:

        grab = input("Do you want to grab it? (y/n): ").lower()

        if grab == "y":
            if len(inventory_list) == 4:
                print("You can't carry any more items. Drop something first. ")
                break
            else:
                inventory_list.append(inventory[item - 1])
                write_items(inventory_list)
                print(f"You picked up {inventory[item - 1]}.")
                break
        elif grab == "n":
            break
        else:
            print("Invalid value. Try again. ")


def drop_item(inventory_list):
    if len(inventory_list) == 0:
        print("There's nothing to drop. ")
        return

    while True:

        try:

            item_number = int(input("Number: "))

        except ValueError:
            print("Invalid item number. Try again. ")
            continue

        if 0 < item_number <= len(inventory_list):
            item = inventory_list.pop(item_number - 1)
            write_items(inventory_list)
            print(f"You dropped {item}. ")
            break
        else:
            print("There's no item with that number. Try again. ")


def main():

    display_title()

    display_menu()

    inventory = read_current_items()

    while True:

        command = input("Command: ").lower()

        if command == "walk":
            grab_item(inventory)
        elif command == "show":
            show_items(inventory)
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
