
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
lOOPS

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


'''NO 12
- The Fibonacci numbers are the sequence below, where the first two numbers are 1,
and each number thereafter is the sum of the two preceding numbers. Write a
program that asks the user how many Fibonacci numbers to print and then prints
that many. eg-> 1,1,2,3,5,8,13,21,34,55,89... 
'''
def fibonacci(n):
    n1 = 0
    n2 = 1
    count = 0
    while count < n:
        print(n2)
        new_num = n1 + n2
        n1 = n2
        n2 = new_num
        count += 1

fibonacci(6)


'''NO 13
- Use a for loop to print a triangle like the one below. Allow the user to specify
how high the triangle should be. 
* 
**
*** 
**** 
'''
tri_height = int(input("\nEnter the height of your triangle: "))
count = 1
while count < tri_height + 1:
    print("*" * count)
    count += 1


'''NO 14
- Use a for loop to print a triangle like the one below. Allow the user to specify
how high the triangle should be.
**** 
***
** 
* 
'''
tri_height2 = int(input("\nEnter the height of your triangle: "))
count = tri_height2
while count > 0:
    print("*" * count)
    count -= 1


'''NO 15
- Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down,
ask them to enter a number below 20 and then count down from 20 to that number.
If they entered something other than up or down, display the message
“I don't understand”. 
'''
count_from = input("\nWhere do you want to count from(up/down): ")
if count_from.lower() == "up":
    top_num = eval(input("Enter your top number: "))
    for number in range(1, top_num+1):
        print(number)
elif count_from.lower() == "down":
    down_num = eval(input("Enter a number below 20: "))
    for number in range(20, down_num-1, -1):
        print(number)
else:
    print("I don't understand")


'''NO 16
- Ask the user to enter their name and a number. If the number is less than 10,
then display their name that number of times; otherwise display the message “Too high”
three times.
'''
user_name = input("\nEnter your name: ")
user_num = int(input("Enter a number: "))
if user_num < 10:
    for num in range(0, user_num):
        print(user_name)
else:
    for num in range(0, 3):
        print("Too high.")


'''NO 17
-(a) Write a program that uses a while loop (not a for loop) to read through a string
and print the characters of the string one-by-one on separate lines.
(b) Modify the program above to print out every second character of the string.
'''
string = "Confi"
count = 0
while count < len(string):
    print(string[count])
    count += 1

#(b)
string2 = "Worlasi"
count2 = 0
while count2 < len(string):
    print(string2[count2])
    count2 += 2


'''NO 18
- A good program will make sure that the data its users enter is valid.
Write a program that asks the user for a weight and converts it from kilograms
to pounds. Whenever the user enters a weight below 0, the program should tell them
that their entry is invalid and then ask them again to enter a weight.
[Hint: Use a while loop, not an if statement].
'''
count = 0
while count < 1:
    weight_in_kg2 = float(input("\nEnter weight in kilogram: "))
    if weight_in_kg2 > 0:
        weight_in_pounds2 = weight_in_kg2 * 2.2
        print(f"Your weight in pounds is: {round(weight_in_pounds2, 2)}lbs")
        count += 1
    else:
        print("Wrong entry.")


'''NO 19
- Recall that, given a string s, s.index('x') returns the index of the first x in s
and an error if there is no x.
(a) Write a program that asks the user for a string and a letter. Using a while loop,
the program should print the index of the first occurrence of that letter and a message
if the string does not contain the letter.
(b) Write the above program using a for/break loop instead of a while loop.
'''

# Using while loop
str = input("\nEnter any string: ")
letter = input("Enter a letter of the alphabet.: ")

check = True
while check:
    if letter in str:
        print(str.index(letter))
        check = False
    else:
        print(f"{letter} not in {str}.")
        break

# Using for/break loop
for i in range(len(str)):
    if letter in str:
        print(str.index(letter))
        break
    else:
        print(f"{letter} not in {str}.")
        break


'''NO 20
Write a program that allows the user to enter any number of test scores.
The user indicates they are done by entering in a negative number. Print how many
of the scores are A's (90 or above). Also print out the average.
'''

test_score = []
again = True

while again:
    print("\nEnter a negative number when done.")
    user_input = int(input("Enter test score: "))
    if user_input >= 0:
        test_score.append(user_input)
    else:
        again = False


count = 0
average = 0
sum = 0
for i in test_score:
    sum += i
    if i >= 90:
        count += 1


average = sum/len(test_score)
print(f"{count} test scored 'A'.\nAverage is: {average}")


'''NO 21
FUNCTIONS

Write a function called change_case that given a string, returns a string with each
upper case letter replaced by a lower case letter and vice-versa.
'''

def change_case(str):
    change = list()
    for i in str:
        if i == i.lower():
            change.append(i.upper())
        if i == i.upper():
            change.append(i.lower())
        str = "".join(change)
    return str

print(change_case("conFiDeNcE"))


'''NO 22
Write a function called is_sorted that is given a list and returns True if the list
is sorted and False otherwise. 
'''
def is_sorted(list):
    sort_list = sorted(list)
    if list == sort_list:
        return True
    else:
        return False

names = ["Mary", "James", "Mike", "Eva", "Sandra", "Angela"]
num = [5, 11, 4, 105, 25, 87, 2]

print(is_sorted(names))
print(is_sorted(num))


'''NO 23
Write a function called one_away that takes two strings and returns True
if the strings are of the same length and differ in exactly one letter,
like bike/hike or water/wafer.
'''
def one_way(str1, str2):
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return True
            else:
                return False
    else:
        return f"Words are not the same length."
    
print(one_way("bike", "hike"))


'''NO 24
- Write a function called first_diff that is given two strings and returns the first
location in which the strings differ.
If the strings are identical, it should return -1.
'''
def first_diff(str1, str2):
    _min = min(len(str1), len(str2))
    for i in range(_min):
        if str1[i] != str2[i]:
            return i
    
    if str1 == str2:
        return -1

print(first_diff("hoke", "hike"))


'''NO 25
- The digital root of a number n is obtained as follows: Add up the digits n to get a
new number. Add up the digits of that to get another new number. Keep doing this until
you get a number that has only one digit. That number is the digital root.For example,
if n = 45893, we add up the digits to get 4+5+8+9+3 = 29. We then add up the digits of
29 to get 2+9=11. We then add up the digits of 11 to get 1+1=2. Since 2 has only one
digit, 2 is our digital root. Write a function that returns the digital root of an
integer n.
'''
def digital_root(n):
    result = 0
    digital_r = 0

    for digit in str(n):
        result += int(digit)
    
    if result in range(1, 10):
        digital_r = result
    else:
         digital_r = digital_root(result)

    return digital_r


print(digital_root(45893))


'''NO 26
Write a function called matches that takes two strings as arguments and returns how many matches there
are between the strings. 
A match is where the two strings have the same character at the same index. For instance, 
'python' and 'path' match in the first, third, and fourth characters, so the function
should return 3
'''

def matches(str1, str2):
    _match = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                _match = _match + str1[i]
    return _match, len(_match)

print(matches("python", "path"))



'''NO 27
Implement a function called duplicate_count that takes a
string as input and returns the count of characters that
appear more than once in the string. The count should be
case-insensitive.
'''
from collections import Counter
from string import punctuation


# SOLUTION 1
def duplicate_count(str):
    # remove all punctuations
    for punc in punctuation:
        str = str.replace(punc, "")
    
    str = str.lower() # convert string to lower case
    
    # Count the occurrences of each character in the string
    char_count = Counter(str)

    count = 0
    for key, value in char_count.items():
        if value > 1:
            count = value
            print(f"{key} appear {count} times")
    return duplicate_count

duplicate_count("functionally")
duplicate_count("This is a sentence string.")


# # SOLUTION 2
def duplicate_count(str):
    str = str.lower()  # Convert string to lowercase
    char_count = {}  # Dictionary to store character counts

    # Count the occurrences of each character in the string
    # modified
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1

    # Counting the characters that appear more than once    
    count = 0
    for key, value in char_count.items():
        if value > 1:
            count = value
            print(f"{key} appear {count} times")
    return duplicate_count

duplicate_count("functionally now is not safe.")


# SOLUTION 3 - displays the character and the number of times they appear.
def get_repeated_characters(str):
    str = str.lower()
    char_counts = Counter(str)
    
    for key, value in char_counts.items():
        if value > 1:
            print(f"{key} appears {value} times")
    
    return get_repeated_characters

get_repeated_characters("This is a string.")



'''NO28'''