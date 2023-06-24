from collections import Counter
from string import punctuation

'''NO 1
Write a function called matches that takes two strings as arguments and returns how many matches there
are between the strings. 
A match is where the two strings have the same character at the same index. For instance, 
'python' and 'path' match in the first, third, and fourth characters, so the function should return 3
'''
def matches(str1, str2):
    _match = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                _match = _match + str1[i]
    return _match, len(_match)

print(matches("python", "path"))


'''NO 2
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


'''NO 3
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


'''NO 4
Implement a function called duplicate_count that takes a
string as input and returns the count of characters that
appear more than once in the string. The count should be
case-insensitive.
'''
# SOLUTION 1
def duplicate_count(str):
    for punc in punctuation:
        str = str.replace(punc, "")
    
    char_count = Counter(str)

    count = 0
    for value in char_count.values():
        if value > 1:
            count += 1
    return count

print(duplicate_count("function"))
print(duplicate_count("This is a sentence string."))



#SOLUTION 2
def duplicate_count(str):
    str = str.lower()  # Convert string to lowercase
    char_count = {}  # Dictionary to store character counts

#   Count the occurrences of each character in the string
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
        # print(char_count)

#   Counting the characters that appear more than once    
    count = 0
    # for key, value in char_count.items():
    #     if key > 1:
    #         count += 1

    for value in char_count.values():
        if value > 1:
            count += 1
    return count

print(duplicate_count("functions now"))
print(duplicate_count("This is a sentence string."))



#SOLUTION 3 - displays the character and the number of times they appear.
def get_repeated_characters(str):
    char_counts = Counter(str)
    # repeated_chars = [char for char, count in char_counts.items() if count == 2]
    
    for key, value in char_counts.items():
        if value > 1:
            print(f"{key} appears {value} times")

    # num_of_char = 0
    # for i in repeated_chars:
    #     num_of_char += 1

    # return  char_counts

get_repeated_characters("This is a sentence string.")



'''NO 5
Create a function called word_frequency that takes a
sentence as input and returns a dictionary where the keys
are the unique words in the sentence, and the values are
the frequencies of those words.
'''
def word_frequency(str):

    for punc in punctuation:
        str = str.replace(punc, "")
        
    str = str.lower().split()

    word_count = {}
    for word in str:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(word_frequency("I am that i am, no one can see through."))


#SOLUTION 2
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


'''No 6
Write a function called binary_search that takes a sorted
list and a target value as input and returns the index of
the target value in the list. If the target value is not
found, return -1.
'''
def binary_search(s_list, t_value):
    for i in s_list:
        if i == t_value:
            return f"{i} is at index {s_list.index(i)}"


num = [1, 5, 8, 14, 20, 2]
num = sorted(num)
print(num)
print(binary_search(num, 14))



'''NO 7
Create a function called is_unique that takes a string
as input and returns True if all characters in the string
are unique, and False otherwise.
'''
def is_unique(str):
    str = str.lower()
    count_char = {}
    for letter in str:
        count_char[letter] = count_char.get(letter, 0) + 1
    
    print(count_char)
    
    for value in count_char.values():
        if value == 1:
            continue
        else:
            return False 

    return True

print(is_unique("comido"))


'''No 8
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


#SOLUTION 2
def count_number2(id):
    digit_counts = {}

    for digit in str(id):
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1

    for digit, count in digit_counts.items():
        print(f"{digit} - {count}")

count_number2(1122309008)


'''NO 9
RACK YOU BRAIN
data = [
    {'name':'Kwadwo', 'phone':'555-1414', 'email':'kwadwo@mail.net'},
    {'name':'Daniel', 'phone':'555-1618', 'email':'daniel@mail.net'}, 
    {'name':'Akwasi', 'phone':'555-3141', 'email':''}, 
    {'name':'Andy', 'phone':'555-2718', 'email':'andy@mail.net'}
]

(a) Print all the users whose phone number ends in an 8
(b) Print all the users that don’t have an email address listed
'''
data = [
    {'name':'Kwadwo', 'phone':'555-1414', 'email':'kwadwo@mail.net'},
    {'name':'Daniel', 'phone':'555-1618', 'email':'daniel@mail.net'}, 
    {'name':'Akwasi', 'phone':'555-3141', 'email':''}, 
    {'name':'Andy', 'phone':'555-2718', 'email':'andy@mail.net'}
]
# (a)
for item in data:
    for value in item.values():
        if value.endswith("8"):
            print(item)


# (b)
print("\n")
for item in data:
    for value in item.values():
        if value == '':
            print(item)


#SOLUTION 2
# (a) Print all the users whose phone number ends in an 8
for key in data:
  p = key['phone']
  if p[-1] == '8':
    print(f"This user phone number ends with 8: {key}")


# (b) Print all the users that don’t have an email address listed
for key in data:
  email = key['email']
  if email == '':
    print(f"{key} has no EMAIL")



'''NO 10
RACK YOUR BRAINS
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

# (a)
month_name = input("Enter a month name: ").capitalize()
days_in_month = days[month_name]
print(f"There are {days_in_month} days in {month_name}")

# (b)
order = [key for key, _ in days.items()]
order.sort()
print(order)

# (c)
days_with_31 = [key for key, value in days.items() if value == 31]
print(days_with_31)

# (d)
sort_order = sorted(days.items(), key=lambda x:x[1])
sort_orders = sorted(days.items(), key=lambda x: x[1], reverse=True)
print(sort_order)
for item in sort_order:
    print(item[0], item[1])



'''NO 11
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
