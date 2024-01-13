
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
def one_away(str1, str2):

    diff = 0
    
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
    else:
        return f"Words are not the same length."
        
    if diff > 1:
        return False
    else:
        return True
    
print(one_away("biku", "hike"))


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
#SOLUTION 1
def digital_root(number):

     #looping for 'number' to be a single digit
     while number >= 10:
        # 'temp_number' will hold the sum of the digits of current 'number'
        temp_number = 0
        number_copy = number

        #loop to add the digits of current 'number'
        while number_copy > 0:
          #get the last digit of current 'number' and add to 'temp_number'
          temp_number += (number_copy % 10)

          #discard the last digit that was just processed
          number_copy //= 10

        #'number' is now updated to 'temp_number'
        number = temp_number # number -> 45893 -> 29 -> 11 -> 2

     return number

print(digital_root(45893))


#SOLUTION 2
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



'''NO 28
Create a function called word_frequency that takes a
sentence as input and returns a dictionary where the keys
are the unique words in the sentence, and the values are
the frequencies of those words.
'''
# SOLUTION 1
def word_frequency(str):

    for punc in punctuation:
        str = str.replace(punc, "")
        
    str = str.lower().split()

    word_count = {}
    for word in str:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(word_frequency("I am that i am, no one can see through."))


# SOLUTION 2
def word_frequency(sentence):
    for punc in punctuation:
        sentence = sentence.replace(punc, "")
    sentence.replace(" ", "")
    sentence = sentence.split()
    
    word_counts = {}
    for word in sentence:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1        

    return word_counts

sen = "I will go, then come, then leave, then sleep, then leave."
print(word_frequency(sen))


'''No 29
Write a function called binary_search that takes a sorted
list and a target value as input and returns the index of
the target value in the list. If the target value is not
found, return -1.
'''
def binary_search(s_list, t_value):
    for i in s_list:
        if i == t_value:
            return f"{i} is at index {s_list.index(i)}"
        else:
            return -1


num = [1, 5, 14, 17, 20, 2]
num = sorted(num)
print(num)
print(binary_search(num, 15))



'''NO 30
Create a function called is_unique that takes a string
as input and returns True if all characters in the string
are unique, and False otherwise.
'''
def is_unique(str):
    str = str.lower()
    count_char = {}
    for letter in str:
        count_char[letter] = count_char.get(letter, 0) + 1
    
    # print(count_char)
    for value in count_char.values():
        if value == 1:
            continue
        else:
            return False 

    return True

print(is_unique("comidi"))


'''No 31
Write a function that accepts an id number and return a count
of each digit in the number
Eg: 1122334
1-2
2-2
3-2
4-1

Iteration | Number | digit |
--------------------------------
0         | 1234   |  NA
1         | 1234   | 4
2         | 123    | 3
3         | 12     | 2
4         | 1      | 1
5         | 
'''

# SOLUTION 1
def count_number(number):
    my_list = []
    for i in range(0, 10):
        my_list.append(0)
    
    while (number > 0):
        current_digit = number % 10
        current_count = my_list[current_digit] + 1
        my_list[current_digit] = current_count
        number = number//10
    
    for i in range(len(my_list)):
        print(f"{i} - {my_list[i]}")

count_number(11223)

# SOLUTION 2
def count_number2(id):
    digit_counts = {}

    for digit in str(id):
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1

    for digit, count in digit_counts.items():
        print(f"{digit} - {count}")

count_number2(11300922082)


'''NO 32
data = [
    {'name':'Kwadwo', 'phone':'555-1414', 'email':'kwadwo@mail.net'},
    {'name':'Daniel', 'phone':'555-1618', 'email':'daniel@mail.net'}, 
    {'name':'Akwasi', 'phone':'555-3141', 'email':''}, 
    {'name':'Andy', 'phone':'555-2718', 'email':'andy@mail.net'}
]

(a) Print all the users whose phone number ends in an 8
(b) Print all the users that don't have an email address listed
'''
data = [
    {'name':'Kwadwo', 'phone':'555-1414', 'email':'kwadwo@mail.net'},
    {'name':'Daniel', 'phone':'555-1618', 'email':'daniel@mail.net'}, 
    {'name':'Akwasi', 'phone':'555-3141', 'email':''}, 
    {'name':'Andy', 'phone':'555-2718', 'email':'andy@mail.net'}
]
# (a) i
for item in data:
    for value in item.values():
        if value.endswith("8"):
            print(item)

    # ii
for item in data: # efficiency
    if item["phone"][-1] == "8":
        print(item)


# (b) i
print("\n")
for item in data:
    for value in item.values():
        if value == '':
            print(item)

    # ii
for item in data: #efficiency
    if item["email"] == "":
        print(item)


# #SOLUTION 2
# (a) Print all the users whose phone number ends in an 8
for key in data:
  p = key['phone']
  if p[-1] == '8':
    print(f"Users whose phone number ends with 8: {key}")


# (b) Print all the users that don’t have an email address listed
for key in data:
  email = key['email']
  if email == '':
    print(f"{key} has no email")



''''NO 33
days = {
    'January':31, 'February':28, 'March':31,'April':30, 'May':31, 'June':30,
    'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31
    }
(a) Ask the user to enter a month name and use the dictionary to tell
them how many days are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month

'''

days = {
    'January':31, 'February':28, 'March':31,'April':30, 'May':31, 'June':30,
    'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31
    }

# (a) Ask the user to enter a month name and use the dictionary to tell
    # them how many days are in the month.
month_name = input("Enter a month name: ").capitalize()
days_in_month = days[month_name]
print(f"There are {days_in_month} days in {month_name}")

# (b) Print out all of the keys in alphabetical order.
order = [key for key, _ in days.items()]
order.sort()
print(order)

# (c) Print out all of the months with 31 days.
days_with_31 = [key for key, value in days.items() if value == 31]
print(days_with_31)

# (d) Print out the (key-value) pairs sorted by the number of days in each month
sort_order = sorted(days.items(), key=lambda x:x[1])
sort_orders = sorted(days.items(), key=lambda x: x[1], reverse=True)
print(sort_order)
for item in sort_order:
    print(item[0], item[1])



'''NO 34
Write a program that repeatedly asks the user to enter product
names and prices.

Store all of these in a dictionary whose keys are the product
names and whose values are the prices.

When the user is done entering products and prices, allow them
to repeatedly enter a product name and print the corresponding price
or a message if the product is not in the dictionary.
'''

product = {}
again = True
while again:
    response = int(input('''
    Select  1 to enter new product
            2 to check product
            0 to quit: '''))
    
    if response == 1:
        add_product =  input("\n\tEnter product name: ")
        add_price =  int(input("\n\tEnter price: "))
        product[add_product] = add_price
        print(product)
    
    elif response == 2:
        check_product =  input("\n\tEnter product name: ")
        if check_product in product.keys():
            print(f"{check_product} = {product[check_product]}")
        else:
            print("Item is not available.")
    else:
        again == False
        break



'''NO 35
- Write a function called closest that takes a list of numbers L and a number n and
returns the largest element in L that is not larger than n. For instance,
if L=[1,6,3,9,11] and n=8, then the function should return 6, because 6 is the
closest thing in L to 8 that is not larger than 8. Don't worry about if all of the
things in L are smaller than n. 
'''

# My Solution 1
num_list = [3, 6, 8, 1, 17, 9]

def closest(list, n):
    sort_list = sorted(list)
    n_idx = sort_list.index(n)
    small_val_idx = n_idx - 1
    if small_val_idx < 0:
        return f"No number is smaller than {n} in the list."
    else:
        return sort_list[small_val_idx]

print(closest(num_list, 1))


'''NO 36
A function that calculates the average score for a list of student scores. 
'''
def calc_average(scores):
    total_score = 0
    number_of_scores = len(scores)

    # check for an empty list
    if number_of_scores == 0:
        return 0

    for score in scores:
        total_score += score
    
    average = total_score / number_of_scores
    return round(average,2)

score_list = [56, 75, 92, 88, 56]
print(calc_average(score_list))


'''NO 37
LISTS

- Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the result.
(g) Print how many integers in the list are less than 5.
'''
list_of_int = list()
print("\nYou are creating a list of integers.")
number_of_items = int(input("How many integers do you want in your list?: "))
count = 0
while count < number_of_items:
    num = int(input("Enter number: "))
    list_of_int.append(num)
    count += 1

# (a) Print the total number of items in the list.
print(f"You have {len(list_of_int)} integers in your list.")

# (b) Print the last item in the list.
print(f"The last item in your list is {list_of_int[-1]}")

# (c) Print the list in reverse order.
len = len(list_of_int)
while len > 0:
    print(list_of_int[len - 1])
    len -= 1

#(d) Print Yes if the list contains a 5 and No otherwise.
if 5 in list_of_int:
    print("Yes")
else:
    print("No")

# (e) Print the number of fives in the list.
count5 = 0
for item in list_of_int:
    if item == 5:
        count5 += 1

print(f"You have {count5} fives in your list.")

# (f) Remove the first and last items from the list, sort the remaining items,
    # and print the result.
list_of_int.remove(list_of_int[0])
list_of_int.remove(list_of_int[-1])
sort_list = sorted(list_of_int)
print(f"This is your sorted list: {sort_list}")

# (g) Print how many integers in the list are less than 5.
countlessthan5 = 0
for item in list_of_int:
    if item < 5:
        countlessthan5 += 1

print(f"There are {countlessthan5} integers less than 5 in your list.")


'''NO 38
- Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
'''
rand_list = list()
count = 20
while count != 0:
    rand_num = random.randint(1, 100)
    if rand_num not in rand_list:
        rand_list.append(rand_num)
        count -= 1
    else:
        continue

sort_rand_list = sorted(rand_list)

# (a) Print the list.
print(sort_rand_list)

# (b) Print the average of the elements in the list.
avg = sum(sort_rand_list)/len(sort_rand_list)
print(f"Average is: {avg}")

# (c) Print the largest and smallest values in the list.
print(f"\nLargest value is: {max(sort_rand_list)}")
print(f"Smallest value is: {min(sort_rand_list)}")

# (d) Print the second largest and second smallest entries in the list
sec_lg = sort_rand_list.index(max(sort_rand_list)) - 1
print(f"\nSecond Largest value is: {sort_rand_list[sec_lg]}")

sec_sm = sort_rand_list.index(min(sort_rand_list)) + 1
print(f"Second Smallest value is: {sort_rand_list[sec_sm]}")

# (e) Print how many even numbers are in the list.
count = 0
for num in sort_rand_list:
    if num % 2 == 0:
        count += 1

print(f"\nThere are {count} even numbers in the list.")



'''NO 39
- Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17 
(b) Add4,5,and 6 to the end of the list 
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
'''
li = [8, 9, 10]

# (a) Set the second entry (index 1) to 17
li[1] = 17
print("\n", li)

# (b) Add 4,5,and 6 to the end of the list
li.append(4)
li.append(5)
li.append(6)
print("\n", li)

# (c) Remove the first entry from the list
del li[0]
print("\n", li)

# (d) Sort the list
sort_li = sorted(li)
print("\n", sort_li)

# (e) Double the list
double_li = sort_li + sort_li
print("\n", double_li)

# (f) Insert 25 at index 3
double_li.insert(3, 25)

# The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
print("\n", double_li)


'''
NO 40
- Write a program that takes any two lists L and M of the same size and adds their elements
together to form a new list N whose elements are sums of the corresponding elements in L and M.
For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].
'''

def add_list(l, m):
    n = list()
    if len(l) == len(m):
        for i in range(len(l)):
            n.append(l[i] + m[i])
    return n

l1 = [3,1,4]
l2 = [1,5,9]

print(add_list(l1, l2))


'''NO 41
- Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run
of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
'''
rand_bi = list()
for num in range(0, 25):
    rand = random.randint(0,1)
    rand_bi.append(rand)
print(rand_bi)

maximum = count = 0
current = 0
for c in rand_bi:
    if c == current:
        count += 1
    else:
        count = 0
    maximum = max(count, maximum)

print(maximum)


'''
NO 42
- Write a program that removes any repeated items from a list so that each item appears at
most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
'''
def remove_duplicate(list_args):
    new_list = list()
    for item in list_args:
        if item not in new_list:
            new_list.append(item)
    
    return new_list

test_list = [1,1,2,3,4,3,0,0]
print(remove_duplicate(test_list))


'''NO 43
- Write a simple quiz game that has a list of ten questions and a list of answers to those
questions. The game should give the player four randomly selected questions to answer.
It should ask the questions one-by-one, and tell the player whether they got the question
right or wrong. At the end it should print out how many out of four they got right.
'''
questions = [
    "What is the capital of Ghana",
    "Who is the current president of USA",
    "How many countries are in Africa",
    "Which country has the largest population",
    "The second most populous country in the world is",
    "How many states are in the United States of America",
    "Python is a high level programming language True/False",
    "WHO is an acronym for World High Organization",
    "How many months are in a year",
    "Ghana gained independence in which year"
]

answers = [
    "Accra", "Joe", "54", "India", "China",
    "52", "True", "False", "12", "1957"
]

count = 0
correct = 0
while count < 4:
    questions_asked = list()
    questions_asked = random.sample(questions, 4)
    
    for quest in questions_asked:
        answer = input(f"\n{quest}?: ")
        idx = questions.index(quest)
        if answer.capitalize() == answers[idx]:
            print("Correct")
            correct += 1
        else:
            print("Wrong")
        count += 1

print(f"You had {correct} questions right.")


'''NO 44 
Write a function that converts a decimal number(base-10) to hexadecimal(base-16).
'''
# FIRST SOLUTION
def convert_to_hex(number):

    #2 if number is 0, return number.
    if number == 0:
        return number
    
    #3 get an absolute value for negative numbers
    negative_num = False
    if number < 0:
        negative_num = True
        number = abs(number)
    
    #3 Rename variable to hold converted hexadecimal number
    converted = []

    while number > 0:
        remainder = number % 16

        if remainder < 10:
            converted.insert(0, str(remainder))
        elif remainder == 10:
            converted.insert(0, 'A')
        elif remainder == 11:
            converted.insert(0, 'B')
        elif remainder == 12:
            converted.insert(0, 'C')
        elif remainder == 13:
            converted.insert(0, 'D')
        elif remainder == 14:
            converted.insert(0, 'E')
        else:
            converted.insert(0, 'F')

        number //= 16

    hex_num = ''.join(converted)

    if negative_num:
        hex_num = '-' + hex_num

    return hex_num


# Test examples
print(convert_to_hex(16))    # Output: "10"
print(convert_to_hex(-10))   # Output: "-A"
print(convert_to_hex(255))   # Output: "FF"
# more test cases
print(convert_to_hex(-167))   # Output: "-A7"
print(convert_to_hex(0))   # Output: "0"


'''No 45
Voter Registry Cleanup

During an audit of the electoral commission of the nation of Mackie, it was discovered that some people
registered more than once to vote. In the voter registry, a citizen is identified by the social security
number assigned to them from birth. The commission has been tasked to find the actual number of eligible
Mackie citizens who are eligible to vote. Your task is to write a program that, given a list of social
security numbers, can achieve this.

Additionally, the commission wants to identify the individuals who registered more than once and prosecute them,
as it is illegal to register more than once. Your task is to write a program that, given a list of social security
numbers, achieves both goals.

Input:
['123456789', '987654321', '555555555', '123456789', '111111111']

Output:
Actual number of eligible voters: 4
Voters who registered more than once: 123456789
'''
def find_eligible(id_list):
  # a set variable to hold id's to avoid duplicates
  unique_list = set()

  # a list variable to hold id's that are registered more than once.
  multiple_id = list()

  # a loop to check for unique id's and id's that appear more than once.
  for id in id_list:
    if id in unique_list:
      multiple_id.append(id) # append duplicate id's to multiple_id
    else:
      unique_list.add(id) # add unique id's to unique_id

  # getting the number of unique registered id's
  unique_list_length = len(unique_list)

  # a formated string containing the length of eligible and duplicate voters.
  output_string = f'''
  Actual number of eligible voters: {unique_list_length}
  Voters who registered more than once: {multiple_id}
  '''

  # return formated string
  return output_string


# Test case - empty list
ssn_list = []
# Test case - list with one or more elements
ssn_list1 = ['123456789']
ssn_list2 = ['123456789', '987654321', '555555555', '123456789', '111111111']
ssn_list3 = ['123456789', '987654321', '555555555', '123456789', '111111111', '555555555', '010342433']

print(find_eligible(ssn_list))
# print(find_eligible(ssn_list1))
# print(find_eligible(ssn_list2))
# print(find_eligible(ssn_list3))



'''No 46
Title: Duplicate Letter Detector ==>Problem Statement:

You are developing a spelling checker application that needs to identify the first letter in a
given word that appears twice. Your task is to write a Python function that takes a string containing
lowercase English letters and returns the first letter that appears twice in the word.

Instructions:
Implement a Python function find_first_duplicate(s) that takes the following argument:

s: A string consisting of lowercase English letters.
The function should return the first letter that appears twice in the string s. If no letter
appears twice, return None.

''' 

def find_first_duplicate(string):
   dupes = set()

   for character in string:
     if character in dupes:
        return character
     else:
        dupes.add(character)

   return None

# Example:
word1 = "mississippi"
result1 = find_first_duplicate(word1)
print(result1)  # Output: 'i'

word2 = "ghana"
result2 = find_first_duplicate(word2)
print(result2)  # Output: 'a'

word3 = "clean"
result3 = find_first_duplicate(word3)
print(result3)  # Output: 'None'


'''NO 47
DATA STRUCTURE AND ALGORITHMS
TITLE: Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four
numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an
ascending order. If such a quadruplet doesn't exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You're asked to return the first one
you encounter (considering the results are sorted).

Input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
Expected Output: [0, 4, 7, 9] 
'''
# Solution inspired by promp.
def find_array_quadruplet(arr, s):
    n = len(arr)

    # if there are fewer than 4 items in arr, by
    # definition no quadruplet exists whose sum is s
    if n < 4:
        return []

    # sort arr in an ascending order
    arr.sort()
    
    for i in range(0, n - 4):
        for j in range(i + 1, n - 3):
            # r stores the complementing sum
            r = s - (arr[i] + arr[j])

            # check for sum r in subarray arr[j+1…n-1]
            low = j + 1
            high = n - 1

            while low < high:
                if (arr[low] + arr[high]) < r:
                    low += 1

                elif (arr[low] + arr[high]) > r:
                    high -+ 1

                # quadruplet with given sum found
                else:
                    return [arr[i], arr[j], arr[low], arr[high]]

    return []
