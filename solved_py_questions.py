# from collections import Counter
# from string import punctuation

'''
VARIABLES AND CONDITIONALS

NO 1
Write a program that asks the user to enter three numbers
(use three separate input state-ments).
Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.	
'''
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

total  = num1 + num2 + num3
average = total/3

print(f"Total: {total}")
print(f"Average: {average}")


'''NO 2
- A lot of cell phones have tip calculators. Write one. Ask the user for the price
of the meal and the percent tip they want to leave. Then print both the tip amount
and the total bill with the tip included.
'''
price = int(input("\nEnter food price: "))
percent_tip = int(input("Enter percent of tip you want to leave: "))

tip = (percent_tip/price) * 100
total_bill = price + tip

print(f"Tip amount: ${tip}")
print(f"Total bill: ${total_bill}")


'''NO 3
- Write a program that asks the user for a weight in kilograms and converts it to
pounds. There are 2.2 pounds in a kilogram.
'''
weight_in_kg = float(input("\nEnter weight in kilogram: "))
weight_in_pounds = weight_in_kg * 2.2
print(f"Your weight in pounds is: {round(weight_in_pounds, 2)}lbs")



'''NO 4
- Write a program that outputs 100 lines, numbered 1 to 50, each with your name on it.
The output should look like the output below.
1 Your name
2 Your name
3 Your name
.
.
.
50 Your name
'''

num = 1
while num < 51:
    print(f"{num} Worlasi.")
    num += 1



'''NO 5
- Write a program that asks the user to enter a length in centimeters .If the user
enters a negative length, the program should tell the user that the entry is invalid.
Otherwise, the program should convert the length to inches and print out the result.
There are 2.54 centimeters in an inch.
'''
length = int(input("\nEnter a length in centimeters: "))
if length < 1:
    print("Your entry is invalid.")
else:
    convert = length * 2.54









