TAX_RATE = .06


def calculate_sales_tax(amount):
    return round(amount * TAX_RATE, 2)


def calculate_total_after_tax(amount, sales_tax):
    return round(amount + sales_tax, 2)
