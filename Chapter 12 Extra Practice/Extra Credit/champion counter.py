#! /usr/bin/env python3

import csv

FILENAME = "world_cup_champions.txt"


def display_title():
    print("FIFA World Cup Winners\n")


def read_file():

    world_cup_winners = []

    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            world_cup_winners.append(row)

    world_cup_winners.pop(0)

    return world_cup_winners


def count_world_cup_wins(world_cup_winners):

    # Define a dictionary that stores the
    # number of world cup wins for each team

    world_cup_wins = {}

    for row in world_cup_winners:
        for item in row:
            if item == row[1]:
                if item in world_cup_wins:
                    world_cup_wins[item] += 1
                else:
                    world_cup_wins[item] = 1

    return world_cup_wins


def display_world_cup_wins(world_cup_wins, world_cup_winners):
    print("Country\t\t ", "\tWins ", "Years")
    print("=" * 7, "\t   ", "=" * 4, "", "=" * 5)

    countries = list(world_cup_wins.keys())
    countries.sort()

    format_str = "{:<15} {:<5} {:<10}"
    for country in countries:
        years = ""
        year_count = 0
        for row in world_cup_winners:
            for item in row:
                if item == row[0] and country == row[1]:
                    if year_count == 0:
                        years += item
                        year_count += 1
                    elif year_count >= 1:
                        years += ", " + item
                        year_count += 1

        print(format_str.format(country, world_cup_wins[country], years))


def main():

    display_title()

    world_cup_winners = read_file()

    world_cup_wins = count_world_cup_wins(world_cup_winners)

    display_world_cup_wins(world_cup_wins, world_cup_winners)


if __name__ == "__main__":
    main()
