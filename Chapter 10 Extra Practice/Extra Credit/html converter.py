#! /usr/bin/env python3

FILENAME = "groceries.html"


def display_title():
    print("HTML Converter\n")


def read_grocery_list():
    with open(FILENAME) as file:
        lines = file.read()

    lines = lines.replace("     ", "", 3)

    lines = lines.replace("<h1>", "")
    lines = lines.replace("</h1>", "")

    lines = lines.replace("<li>", "* ", 3)
    lines = lines.replace("</li>", "", 3)

    lines = lines.replace("<ul>", "")
    lines = lines.replace("</ul>", "")

    lines = lines.strip()

    grocery_list = lines.split("\n")
    return grocery_list


def main():

    display_title()

    grocery_list = read_grocery_list()

    grocery_list = "\n".join(grocery_list)

    grocery_list = grocery_list[:12] + grocery_list[13:]

    print(grocery_list, end="")


if __name__ == "__main__":
    main()
