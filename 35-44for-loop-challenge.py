### CHALLENGES AFTER LESSON ON [FOR LOOP] ###
'''
No35
Ask the user to enter their name and then display their name
three times.
'''
print("\n")
name = input("Enter your name: ")
for i in range(0, 3):
    print(name.title())

'''
No36
Alter program No35 so that it will ask the user to enter their
name and a number and then display their name that number of times.
'''
print("\n")
name = input("Enter your name: ")
num = int(input("Enter a number: "))
for i in range(0, num):
    print(name.title())

'''
No37
Ask the user to enter their name and display each letter in their
name on a separate line
'''
print("\n")
name = input("Enter your name: ")
for letter in name:
    print(letter)

'''
No38
Change program No37 to ask for a number. Display their name
(one letter at a time on each line) and repeat this for the
number of times they entered
'''
print("\n")
num = int(input("Enter a number: "))
name = input("Enter your name: ")
for number in range(0, num):
    for letter in name:
        print(letter)

'''
No39
Ask the user to enter a number between 1 and 12 and then
display the times table for that number.
'''
print("\n")
num = eval(input("Enter a number between 1 and 12: "))
for number in range(1, 13):
    answer = num*number
    print(f"{num} x {number} = {answer}")

'''
No40
Ask for a number below 50 and then count down from 50 to
that number, making sure you show the number they entered
in the output
'''
num = eval(input("Enter a number below 50: "))
print(f"Counting down from 50 to {num}")
for number in range(50, num-1, -1):
    print(number)

'''
No41
Ask the user to enter their name and a number. if the number
is less than 10, then display their name that number of times;
otherwise display the message "Too high" three times.
'''
print("\n")
name = input("Enter your name: ")
num = eval(input("Enter a number: "))
if num < 10:
    for number in range(0, num):
        print(name.title())
else:
    for number in range(0, 3):
        print("Too high")

'''
No42
Set a variable called total to 0. Ask the user to enter five
numbers and after each input ask them if they want that number
included. If they do, then add the number to the total. If they
do not want it included, don't add it to the total. After they
have entered all five numbers, display the total.
'''
print("\n")
total = 0
print("You will enter five numbers")
for number in range(1, 6):
    num = eval(input("Enter number: "))
    consent = input("Do you want number to be included(y/n): ")
    if consent == "y":
        total = total + num
print(total)

'''
No43
Ask which direction the user wants to count (up or down). If they
select up, then ask them for the top number and count from 1 to
that number. if they select down, ask them to enter a number
below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message
"I don't understand".
'''
print("\n")
count_from = input("Where do you want to count from(up/down): ")
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

'''
No44
Ask how many people the user wants to invite to a party. If they
enter a number below 10, ask for the names and after each name
display "[name] has been invited". If they enter a number which
is 10 or higher, display the message "Too many people".
'''
print("\n")
people = eval(input("How many people do you want to invite: "))
if people < 10:
    for number in range(0, people):
        names = input("Enter name: ")
        print(f"{names.title()} has been invited.")
else:
    print("Too many people.")