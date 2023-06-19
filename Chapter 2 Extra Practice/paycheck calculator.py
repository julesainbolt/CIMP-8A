#! /usr/bin/env python3

print("Pay Check Calculator\n")

# User input
hours_worked = float(input("Hours Worked:\t "))
hourly_pay_rate = float(input("Hourly Pay Rate: "))

# Calculate and display gross pay
gross_pay = hours_worked * hourly_pay_rate
print(f"\nGross Pay: \t\t {round(gross_pay, 2)}")

# Display the tax rate
tax_rate = 18
print(f"Tax Rate: \t\t {tax_rate}%")

# Calculate and display tax amount
tax_amount = gross_pay * (tax_rate / 100)
print(f"Tax Amount: \t {round(tax_amount, 2)}")

# Calculate and display take home pay
take_home_pay = gross_pay - tax_amount
print(f"Take Home Pay: \t {round(take_home_pay, 2)}")
