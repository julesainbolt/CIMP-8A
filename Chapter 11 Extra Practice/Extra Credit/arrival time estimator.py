#! /usr/bin/env python3

from datetime import datetime


def display_title():
    print("Arrival Time Estimator\n")


def get_estimated_departure_date():
    departure_date_str = input("Estimated date of departure (YYYY-MM-DD): ")
    departure_date = datetime.strptime(departure_date_str, "%Y-%m-%d")
    return departure_date


def get_estimated_departure_time():
    departure_time_str = input("Estimated time of departure (HH:MM AM/PM): ")
    departure_time = datetime.strptime(departure_time_str, "%I:%M %p")
    return departure_time


def get_miles():
    return int(input("Enter miles: "))


def get_miles_per_hour():
    return int(input("Enter miles per hour: "))


def main():

    display_title()

    continue_program = "y"
    while continue_program.lower() == "y":

        # User input
        departure_date = get_estimated_departure_date()
        departure_time = get_estimated_departure_time()

        miles = get_miles()
        mph = get_miles_per_hour()

        print("\nEstimated travel time")

        # Calculate and display hours and minutes
        hours = miles / mph

        hours_to_minutes = hours * 60
        hours = hours_to_minutes // 60
        minutes_remaining = hours_to_minutes % 60

        print(f"Hours: {int(hours)}")
        print(f"Minutes: {int(minutes_remaining)}")

        arrival_hour = departure_time.hour + int(hours)

        if departure_time.strftime("%p") == "PM" and arrival_hour > 24:
            if departure_time.minute + int(minutes_remaining) > 59:
                arrival_date_time = datetime(departure_date.year, departure_date.month,
                                             departure_date.day, int(arrival_hour - 24) + 1,
                                             int(minutes_remaining) - departure_time.minute)
            else:
                arrival_date_time = datetime(departure_date.year, departure_date.month,
                                             departure_date.day + 1, arrival_hour - 24,
                                             departure_time.minute + int(minutes_remaining))
        else:
            if departure_time.minute + int(minutes_remaining) > 59:
                remaining_minutes_in_hour = 60 - departure_time.minute
                minutes_in_new_hour = minutes_remaining - remaining_minutes_in_hour
                arrival_date_time = datetime(departure_date.year, departure_date.month,
                                             departure_date.day, int(arrival_hour) + 1,
                                             int(minutes_in_new_hour))
            else:
                arrival_date_time = datetime(departure_date.year, departure_date.month,
                                             departure_date.day, int(arrival_hour),
                                             departure_time.minute + int(minutes_remaining))

        print("Estimated date of arrival: " + arrival_date_time.strftime("%Y-%m-%d"))
        print("Estimated time of arrival: " + arrival_date_time.strftime("%I:%M %p"))

        continue_program = input("\nContinue? (y/n): ")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()
