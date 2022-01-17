"""
File: prove.py
Author: Jonathan Wright

Purpose: prove myself.
"""

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))

sub_total = ((child_meal * float(children)) + (adult_meal * float(adults)))
print(f'\nSubtotal: ${"%.2f" % sub_total}')

sales_tax = float(sub_total * float(tax/100))
print(f'Sales Tax: ${"%.2f" % sales_tax}')

total = float(sub_total + sales_tax)
print(f'Total: ${"%.2f" % total}')

pay = float(input("\nWhat is the payment amount? "))
while pay < total:
    pay = float(input("\nPayment must be more than Total. \nWhat is the payment amount? "))

change = (pay - total)
print(f'Change: ${"%.2f" % change}\n')