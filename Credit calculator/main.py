import math


def interest_rate(x):
    x = x / (12 * 100)
    return x


def count_of_months():
    print("Enter credit principal:")
    p = float(input())
    print("Enter monthly payment:")
    monthly_payment = float(input())
    print("Enter credit interest:")
    i = float(input())
    i = interest_rate(i)
    payment_period = math.ceil(number_of_payments(p, monthly_payment, i))
    if payment_period % 12 == 0:
        if payment_period // 12 > 1:
            print(f"{payment_period // 12} years")
        else:
            print("1 year")
    else:
        if payment_period // 12 == 0:
            print(f"{payment_period} months")
        else:
            print(f"{payment_period // 12} years and {payment_period % 12} months")


def number_of_payments(x, y, z):
    a = math.log((y / (y - z * x)), 1 + z)
    return a


def annuity():
    print("Enter credit principal:")
    p = float(input())
    print("Enter count of periods:")
    count_of_periods = float(input())
    print("Enter credit interest:")
    i = float(input())
    i = (i / 12) / 100
    ordinary_annuity = p * ((i * ((1 + i) ** count_of_periods)) / (((1 + i) ** count_of_periods) - 1))
    print(f"Your annuity payment = {math.ceil(ordinary_annuity)}!")


def credit_principal():
    print("Enter monthly payment:")
    monthly_payment = float(input())
    print("Enter count of periods:")
    count_of_periods = float(input())
    print("Enter credit interest:")
    i = float(input())
    i = (i / 12) / 100
    credit_principal1 = monthly_payment / ((i * ((1 + i) ** count_of_periods)) / (((1 + i) ** count_of_periods) - 1))
    print(f"Your credit principal = {round(credit_principal1)}!")


print(f'''What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal:''')
option = input()
if option == "n":
    count_of_months()
elif option == "a":
    annuity()
else:
    credit_principal()
