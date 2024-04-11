# conditional statements (if/else)
# eg if condition:
#   do this
# else:
# do this

# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("what is your age? "))
#     if age < 12:
#         print("Please pay $5.00")
#     elif age <= 18:
#         print("Please pay $7.00")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride the rollercoaster")


# comparison operators
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to
# ==    equal to
# !=    not equal to


# The modulo is written as a percentage sign (%) in Python.
# It gives you the remainder after a division


# nesting if statement

# if condition:
#   if another condition:
#       do this
#   else:
#       do this
# else:
#   do this

# quiz bmi 2.0

# quiz 2 leap year calculator
# year = int(input())

# FirstCondition = year % 4
# SecondCondition = year % 100
# ThridCondition = year % 400

# if FirstCondition > 0:
#     print("Not leap year")
# elif SecondCondition != 0:
#     print("leap year")
# elif ThridCondition > 0:
#     print("Not leap year")
# else:
#     print("leap year")


# multipe if statement
#    if / elif /else
#   if condition1:
#   do A
#   elif condition2:
#       do B
#   else:
#       do C

# multipe if condition
# if condition1:
#  do A
# if condition2:
#  do B
# if condition3:
#  do C


# another code challenge pizza delivery
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N

bill = 0
if size == "S":
    bill = 15
if size == "M":
    bill = 20
elif size == "L":
    bill = 25

# print(bill)
if add_pepperoni == "Y":
    if bill == 15:
        bill += 2
    elif bill == 20:
        bill += 3
    elif bill == 25:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
