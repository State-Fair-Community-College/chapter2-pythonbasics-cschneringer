# --------------------------------------------
# Name: Caleb Schneringer
# Date: 2/11/2026
# Program: Chapter 2 Practice
# Description:
# Complete each section by following the
# directions in the comments.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Variables and print
# ------------------------------------------------
# TODO:
# 1. Create a variable named name
# 2. Store your name as a string in the variable
# 3. Use print() to display: Hello, <name>

name = "Caleb"
print("hello " + name)  # blank line for readability


# ------------------------------------------------
# Practice 2: Input and output
# ------------------------------------------------
# TODO:
# 1. Ask the user to enter their favorite color
# 2. Store the input in a variable
# 3. Print a sentence that includes the color

fav_color = input("What is your favorite color?: ")
print("your favorite color is " + fav_color)


# ------------------------------------------------
# Practice 3: Adding two numbers
# ------------------------------------------------
# TODO:
# 1. Ask the user for a number
# 2. Convert the input to an integer
# 3. Ask the user for a second number
# 4. Convert the input to an integer
# 5. Add the two numbers together
# 6. Print the total

number = int(input("what number do you choose?: "))
number_2 = int(input("what number do you choose?: "))

combined_number = number + number_2
print("your number is: " + str(combined_number))


# ------------------------------------------------
# Practice 4: Calculations with variables
# ------------------------------------------------
# TODO:
# 1. Ask the user for the price of an item
# 2. Convert the input to a float
# 3. Create a variable for the tax rate (use 0.08)
# 4. Calculate the tax amount
# 5. Calculate the final price
# 6. Print the final price

price = float(input("What price is your item?: "))
tax_rate = 0.08
tax_amount = price*tax_rate
final_price = tax_amount + price

print("your final price is:" + str(final_price))


# ------------------------------------------------
# Practice 5: Formatted output with f-strings
# ------------------------------------------------
# TODO:
# 1. Ask the user how many hours they worked
# 2. Ask the user for their hourly pay
# 3. Convert both inputs to floats
# 4. Calculate weekly pay
# 5. Use an f-string to display the result
#    (Round to 2 decimal places)

hours = float(input("how many hours did you work?: "))
hourly_pay = float(input("what is your hourly pay?: "))
weekly_pay = hours*hourly_pay

print(f"you got ${weekly_pay} this week. ")
