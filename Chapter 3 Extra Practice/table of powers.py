#! /usr/bin/env python3

print("Table of Powers\n")

while True:
    # User input
    start_number = int(input("Start number: "))
    stop_number = int(input("Stop number:  "))

    if start_number > stop_number:
        print("Start number can't be greater than the stop number. "
              "Please try again.")
        continue
    else:
        break

print("\nNumber\t ", "Squared\t ", "Cubed")
print("======\t ", "=======\t ", "=====")

# Calculate and display the squares and cubes
# of the numbers ranging from the start number to the stop number
# that the user entered
for number in range(start_number, stop_number + 1):
    print(number, number ** 2, number ** 3, sep="\t\t  ")
