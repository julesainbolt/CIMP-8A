#! /usr/bin/env python3

from datetime import date, datetime


def display_title():
    print("Birthday Calculator\n")


def get_name():
    return input("Enter name: ")


def get_birth_date():
    birthday_str = input("Enter birthday (MM/DD/YY): ")
    birthday = datetime.strptime(birthday_str, "%m/%d/%y")

    if birthday > datetime.now():
        fixed_birth_year = birthday.year - 100
        birthday = datetime(fixed_birth_year, birthday.month, birthday.day)

    return birthday


def main():

    display_title()

    continue_program = "y"
    while continue_program.lower() == "y":

        # User input
        name = get_name()
        birthday = get_birth_date()

        # Get the current date
        current_date = date.today()

        # Calculate the user's age

        years = 0
        if current_date.month > birthday.month:
            years = current_date.year - birthday.year
        elif current_date.month < birthday.month:
            years = (current_date.year - birthday.year) - 1
        elif current_date.month == birthday.month:
            if current_date.day >= birthday.day:
                years = current_date.year - birthday.year
            else:
                years = (current_date.year - birthday.year) - 1

        age_in_days = (datetime.now() - birthday).days

        # Calculate the number of days until the
        # user's next birthday

        next_birthday = date(current_date.year, birthday.month, birthday.day)

        if current_date > next_birthday:
            next_year = current_date.year + 1
            next_birthday = date(next_year, birthday.month, birthday.day)

        days_until_next_bday = (next_birthday - current_date).days

        format_str = "%A, %B %d, %Y"

        # Display the user's birthday
        print(f"Birthday: " + birthday.strftime(format_str))

        # Display the current date
        print(f"Today: \t  " + current_date.strftime(format_str))

        # Display the user's age

        if years > 2:
            print(f"{name} is {years} years old. ")
        else:
            print(f"{name} is {age_in_days} days old. ")

        # Display the number of days until the
        # user's next birthday

        if current_date.month == birthday.month and \
                current_date.day + 1 == birthday.day:
            print(f"{name}'s birthday is tomorrow!")
        elif current_date.month == birthday.month and \
                current_date.day - 1 == birthday.day:
            print(f"{name}'s birthday was yesterday!")
        elif current_date.month == birthday.month and \
                current_date.day == birthday.day:
            print(f"{name}'s birthday is today!")
        else:
            print(f"{name}'s birthday is in {days_until_next_bday} days. ")

        continue_program = input("\nContinue? (y/n): ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
