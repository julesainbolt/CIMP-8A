#! /usr/bin/env python3

print("Letter Grade Converter\n")

continue_program = "y"
while continue_program.lower() == "y":
    number_grade = int(input("Enter numerical grade: "))

    if 88 <= number_grade <= 100:
        print("Letter grade: A")
    elif 80 <= number_grade <= 87:
        print("Letter grade: B")
    elif 67 <= number_grade <= 79:
        print("Letter grade: C")
    elif 60 <= number_grade <= 66:
        print("Letter grade: D")
    else:
        print("Letter grade: F")

    continue_program = input("\nContinue? (y/n): ")
    print()

print("Bye!")
