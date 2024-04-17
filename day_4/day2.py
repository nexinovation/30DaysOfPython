# what if i want to calculate the number of number in a lidt of number,
# Data type.

# String type.

# print("Hello"[4])

# print("123" + "345")

# integers.

# print(123 + 345)

# 123_456_789

# float.

# 3.14159

# boolean.

# True
# False


# to check the data type you are working with you use the TYPE() function.

# numchar = len(input("what is your name? "))
# # print(type(numchar))

# # you can change the data type of integers to strings.
# newnumchar = str(numchar)
# print("your name has " + newnumchar + " characters")

# you can convert different data types.

# a = float(123)
# print(type(a))

# # print(70 + float("100.5"))
# print(str(70) + str(100))


# matimatical expresion.
# 3 + 5 addition
# 7 - 4 subtraction
# 3 * 2 multiplication
# 6 / 3 division
# 2 ** 2 exponent
# 20 % 2 modulo i.e to check for remainder of a number

# in python we have a order in which the matimatical opertion are executed.

# PEMDAS.
# () parentheses
# ** exponent
# * multiplication
# / division
# + addition
# - subtraction

# print(int(3 * (3 + 3) / 3 - 3))


# how to round numbers to integer eg. 2.5 would be rounded to 3,
# and to do this we use the round function.

# print(round(8 / 3))

# you can also round a number to a specific precision in decimal places.
# like if i want to round it to 2 decimal places i would use the (,) and right the number of places i eant to round it to.

# print(round(8 / 3, 2))

# instead of saying divinding (/) i can also use the floor division where i have two forward slashes (//).


# f strings
# instead of doing this with the plus sign you can use the f string
# score = 0

# print("yourscore is " + str(score))

# # eg
# score = 0
# height = 1.8
# iswinning = True
# # f strings
# print(
#     f"your score is {score}, your hight is {height}, your are winning is {iswinning}")


# day 2 final project a tip calculator.
print("Welcome to the tip calculator")
initialBill = float(input("What was your total bill? $"))
amountOfTip = int(
    input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("how many people to split the bill? "))

finaltip = (initialBill / split) * (1 + amountOfTip / 100)
total = round(finaltip, 2)
# finaltip = amountOfTip / 100 * initialBill + initialBill
# total = round(finaltip / split, 2)
# finaltip = amountOfTip / 100
# bill = initialBill * finaltip
# totalamount = initialBill + bill
# result = totalamount / split
# total = round(result, 2)

print(f"Each person should pay: ${total}")
# print(type(initialBill))
