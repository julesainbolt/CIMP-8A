#! /usr/bin/env python3

print("Travel Time Calculator\n")

# user input
miles = int(input("Enter miles: "))
miles_per_hour = int(input("Enter miles per hour: "))

# calculate and display estimated hours and minutes for a trip
print("\nEstimated travel time")
print(f"Hours: {miles // miles_per_hour}")
print(f"Minutes: {miles % miles_per_hour}")
