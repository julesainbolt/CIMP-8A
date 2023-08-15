#! /usr/bin/env python3

import pickle

FILENAME = "birds.bin"


def display_title():
    print("Bird Counter Program\n")


def read_birds():

    birds = {}

    try:
        with open(FILENAME, "rb") as file:
            birds = pickle.load(file)
        return birds
    except EOFError:
        return birds


def write_birds(birds):

    with open(FILENAME, "wb") as file:
        pickle.dump(birds, file)


def display_birds(birds):
    format_str = "{:<15} {:<5}"

    print(format_str.format("Name", "Count"))
    print(format_str.format("=" * 15, "=" * 15))

    bird_names = list(birds.keys())
    bird_names.sort()

    for bird_name in bird_names:
        print(format_str.format(bird_name.title(), birds[bird_name]))


def main():

    display_title()

    birds = read_birds()

    print("Enter 'x' to exit\n")

    while True:

        bird_name = input("Enter name of bird: ").lower()

        if bird_name == "x":
            break

        if bird_name in birds:
            birds[bird_name] += 1
        else:
            birds[bird_name] = 1

    print()

    write_birds(birds)

    display_birds(birds)
            

if __name__ == "__main__":
    main()
