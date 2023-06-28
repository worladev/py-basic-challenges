### CHALLENGES AFTER LESSON ON [NUMERIC ARRAYS] ###

'''
arrays are only used to store numbers.
'i' --> Integer --> whole number between -32,768 and 32,768
'l' --> Long    --> whole number between -2,147,483,648 and 2,147,483,648
'f' --> Floating-point   --> decimals -10^38 to 10^38
'd' --> Double  --> allows decimal places with numbers ranging
        from -10^308 to 10^308

'''
from array import *
import random

print("\n")

# nums = array ('i', [45, 324, 45, 33])
# print(nums)
# print(type(nums))

# for x in nums:
#     print(x)

'''
Array Methods:
.append(variable name), .reverse(), .pop(), sorted(array), .remove(item index)
?.extend(?), .count(item), 
'''


'''No88
Ask the user for a list of five integers. Store them in an array
Sort the list and display it in reverse order.
'''

int_array = array ('i', [])
print("You are creating a list of five integers.")
count = 0
while count < 5:
    user_input = int(input("Enter number: "))
    int_array.append(user_input)
    count += 1
print(int_array)

int_array = sorted(int_array)
print(int_array)

int_array.reverse()
print(int_array)


'''No89
Create an array which will store a list of integers. Generate
five random numbers and store them in the array. Display the array
(showing each item on a separate line).
'''
int_array2 = array ('i', [])
for i in range(0, 5):
    num = random.randint(1, 100)
    int_array2.append(num)

for number in int_array2:
    print(number)


'''No90
Ask the user to enter numbers. If they enter a number between
10 and 20, save it in the array, otherwise display the message
"Outside the range". Once five numbers have been successfully
added, display the message "Thank you" and display the array
with each item shown on a separate line.
'''
int_array3 = array ('i', [])

while len(int_array3) < 5:
    num = int(input("Enter a number: "))
    if num >= 10 and num <= 20:
        int_array3.append(num)
    else:
        print("Outside the range.")

for i in int_array3:
    print(i)


'''No91
Create an array which contains five numbers (two of which should)
be repeated). Display the whole array to the user. Ask the user
to enter one of the numbers from the array and then display
a message saying how many times that number appears in the list.

'''
int_array4 = array ('i', [5, 14, 6, 14, 22])
for i in int_array4:
    print(i)

choice = int(input("Enter a number from the list: "))
no_of_times = int_array4.count(choice)

if no_of_times == 1:
    print(choice, "is in the list once.")
else:
    print(choice, " is in the list ", no_of_times, " times")



'''No92
Create two arrays (one containing three numbers that the user
enters and one containint a set of five random numbers). Join
these two arrays together into one large array
'''
int_array5 = array('i', [])
int_array5b = array('i', [])

for i in range(0, 5):
    generate = random.randint(1, 50)
    int_array5.append(generate)
print(int_array5)

count = 0
while count < 3:
    choice = int(input("Enter a number: "))
    int_array5b.append(choice)
    count += 1
print(int_array5b)

int_array5.extend(int_array5b)
print(int_array5)


'''No93
Ask the user to enter five numbers. Sort them into order and
present them to the user. Ask them to select one of the numbers
Remove it from the original array and save it in a new array.
'''
int_array6 = array('i', [])
new_array = array('i', [])

count = 0
print("Enter 5 numbers.")
while count < 5:
    num = int(input("-->: "))
    int_array6.append(num)
    count += 1

int_array6 = sorted(int_array6)
print(int_array6)
# for i in int_array6:
#     print(i)

selection = int(input("Select one of the numbers: "))
if selection in int_array6:
    int_array6.remove(selection)
    new_array.append(selection)
    print(int_array6)
    print(new_array)
else:
    print("Your number is not in the array.")



'''No94
Display an array of five numbers. Ask the user to select one of
the numbers. Once they have selected a number, display the
position of that item in the array. If they enter something that
is not in the array, ask them to try again until they select a
relevant item.
'''
int_array7 = array('i', [])
for i in range(0, 5):
    int_array7.append(random.randint(1, 25))

print(int_array7)

again = True
while again:
    sel = int(input("Select one of the numbers: "))
    if sel in int_array7:
        position = int_array7.index(sel) + 1
        print(sel, "is in position ", position)
        again = False
    else:
        print("Try again.")


'''No95
Create an array of five numbers between 10 and 100 which each
have two decimal places. Ask the user to enter a whole number
between 2 and 5. If they enter something outside of that
range, display a suitable error message and ask them to try
again until they enter a valid number. Divide each of the
numbers in the array by the number the user entered and display
the answers shown to two decimal places.
'''
int_array8 = array('f', [11.12, 32.01, 13.98, 62.00, 25.65])

again = True
while again:
    user = int(input("Enter a number between 2 an 5: "))
    if user >= 2 and user <= 5:
        for i in range(0, 5):
            ans = int_array8[i]/user
            print(round(ans, 2))
            again = False
    else:
        print("Your number is not in the range\n Try again.")

