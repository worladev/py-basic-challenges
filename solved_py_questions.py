
from collections import Counter
import random
from string import punctuation



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


'''NO 6
- Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the
temperature is in. Your program should convert the temperature to the other unit.
The conversions are F = 9/5 * C + 32 and C = 5/9 * (F - 32).
'''
temp = int(input("\nEnter temperature: "))
unit = input("Celcius or Fahrenheit? (c/f): ")
if unit == "Celcius" or unit == "c" or unit == "C" or unit == "celcius":
    convert_to_fah = (9/5) * temp + 32
    print(f"{temp} C =  {round(convert_to_fah, 2)} F")
elif  unit == "Fahrenheit" or unit == "fahrenheit" or unit == "F" or unit == "f":
    convert_to_cel = (5/9) * (temp - 32)
    print(f"{temp} F =  {round(convert_to_cel, 2)} C")



'''NO 7
- Ask the user to enter a temperature in Celsius. The program should print a message
based on the temperature:
(a) If the temperature is less than -273.15, print that the temperature is invalid because
    it is below absolute zero.
(b) If it is exactly -273.15, print that the temperature is absolute 0.
(c) If the temperature is between-273.15 and 0,print that the temperature is below 
    freezing.
(d) If it is 0, print that the temperature is at the freezing point.
(e) If it is between 0 and 100, print that the temperature is in the normal range.
(f) If it is 100, print that the temperature is at the boiling point.
(g) If it is above 100, print that the temperature is above the boiling point.
'''
temp2 = float(input("\nEnter temperature in Celsius: "))

if temp2 < -273.15:
    print("Temperature is invalid because it is below absolute zero.")
elif temp2 == -273.15:
    print("Temperature is absolute zero.")
elif temp2 > -273.15 and temp2 < 0:
    print("Temperature is below freezing.")
elif temp2 == 0:
    print("Temperature is at the freezing point.")
elif temp2 > 0 and temp2 < 100:
    print("Temperature is in the normal range.")
elif temp2 == 100:
    print("Temperature is at the boiling point.")
else:
    print("Temperature is above the boiling point.")


'''No 8
- Write a program that asks the user how many credits they have taken.
If they have taken 23 or less, print that the student is a freshman.
If they have taken between 24 and 53, print that they are a sophomore.
The range for juniors is 54 to 83, and for seniors it is 84 and over.
'''
credit = int(input("\nHow Many credit have you taken?: "))

if credit <= 23:
    print("You are a freshman.")
elif credit >= 24 and credit <= 53:
    print("You are a sophomore.")
elif credit >= 54 and credit <= 83:
    print("You are a junior.")
elif credit >= 84:
    print("You are a senior.")


'''NO 9
- A store charges $12 per item if you buy less than 10 items. If you buy between
10 and 99 items, the cost is $10 per item. If you buy 100 or more items, the cost
is $7 per item. Write a program that asks the user how many items they are buying
and prints the total cost.
'''
item = int(input("How many item are you buying?: "))
if item < 10:
    cost = item * 12
    print(f"Total cost is ${cost}")
elif item >= 10 and item <= 99:
    cost = item * 10
    print(f"Total cost is ${cost}")
elif item >= 100:
    cost = item * 7
    print(f"Total cost is ${cost}")



'''NO 10
FUNCTIONS AND lOOPS


- Write a program that asks the user to enter a number and prints out all the divisors
of that number.
[Hint:Factors of a number are whole numbers that divide the given number evenly or exactly,
leaving no remainder.]
'''
def get_all_factors(n):
    factors = []
    if n < 0:
        n = -n
    
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(-i)
    return factors
    
print(get_all_factors(4))


'''NO 11
- Write a multiplication game program for kids. The program should give the player
ten randomly generated multiplication questions to do. After each, the program
should tell them whether they got it right or wrong and what the correct answer is.
'''
def multiplication_game():
    print("\nLet us play a multiplication game.")
    again = "y"
    while again == "y":
        first_num = random.randint(0, 15)
        second_num = random.randint(0, 15)
        comp_answer = first_num * second_num

        print("What is the answer for: ")
        user_answer = int(input(f"{first_num} * {second_num} = : "))
        if user_answer == comp_answer:
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct answer is {comp_answer}")
        
        again = input("Type 'y' to play again or 'n' to quit")


multiplication_game()



