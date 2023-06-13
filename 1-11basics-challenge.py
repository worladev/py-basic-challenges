### CHALLENGES AFTER LESSON ON [THE BASICS] ###

# 01 Ask for the user's first name and display the output
    # message Hello [first name]
first_name = input("What is your first name?: ")
print(f"Hello {first_name}")

# 02 Ask for the user's first name and then ask for their
    # surname and display the output message 
    # Hello [first name] [surname]
first_name = input("What is your first name?: ")
surname = input("What is your surname?: ")
print(f"Hello {first_name} {surname}")

# 03 Write a code that will display the joke
# "What do you call a bear with no teeth?" and on the next line
# display the answer "A gummy bear!" Try to create it using only
# one line of code.
print("What do you call a bear with no teeth? \n A gummy bear")

# 04  Ask the user to enter two numbers. Add them together and
# display the anser as The total is [answer]
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
answer = num1 + num2
print(f"The total is: {answer}")

# 05 Ask the user to enter three numbers. Add together the
# first two numbers and then multiply this total by the third
# Display the answer as The answer is [answer]
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
answer = (num1 + num2) * num3
print(f"The total is: {answer}")

# 06 Ask how many slices of pizza the user started with and
# ask how many slices they have eaten. Work out how many
# slices they have left and display the answer in a user
# friendly format.
start_slice = int(input("How many slices of pizza did you start with?: "))
slice_eaten = int(input("How many slice have you eaten?: "))
slice_left = start_slice - slice_eaten
print(f"You have {slice_left} slices of pizza left")

# 07 Ask the user for their name and their age. Add 1 to their
# age and display the output [Name] next birthday you will be
# [new age]
user_name = input("What is your name?: ")
user_age = int(input("What is your age?: "))
new_age = user_age + 1
print(f"{user_name} next birthday you will be {new_age}")

# 08 Ask for the total price of the bill, then ask how many
# diners there are. Divive the total bill by the number of
# diners and show how much each person must pay
total_bill = int(input("What is the total bill?: "))
number_of_diners = int(input("How many diners were there?: "))
shared_bill = total_bill / number_of_diners
print(f"Each person will pay ${shared_bill}.")

# 09  Write a program that will ask for a number of days and
# then will show how many hours, minutes and seconds are
# in that number of days
days = int(input("Enter number of days...: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"In, {days} days, there are ...")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")

# 10 There are 2,204 pounds in a kilogram. Ask the user to
# enter a weight in kilograms and convert it to pounds.
weight_in_kg = int(input("Enter weight in kilogram: "))
pound = weight_in_kg * 2.204
print(f"Your weight is {pound} pounds.")

# 11 Task the user to enter a number over 100 and then enter a
# number under 10 and tell them how many times the smaller number
# goes into the larger number in a user-friendly format.
larger_num = int(input("Enter a number over 100: "))
smaller_num =int(input("Enter a number under 10: "))
answer = larger_num // smaller_num
print(f"{smaller_num} goes into {larger_num} {answer} times")