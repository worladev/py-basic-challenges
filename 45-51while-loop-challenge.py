### CHALLENGES AFTER LESSON ON [WHILE LOOP] ###

'''
No45
Set the total to 0 to start with. While the total is 50 or less,
ask the user to input a number. Add that number to the total
and print the message "The total is...[total]". Stop the loop
when the total is over 50.
'''
print("\n")
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total += num
print(f"The total is...{total}")


'''
No46
Ask the user to enter a number. Keep asking until they enter a
value over 5 and then display the message "The last number you
entered was a [number]" and stop the program.
'''
print("\n")
num = 0
while num <= 5:
    num = int(input("Enter a number: "))
print(f"The last number you entered was a {num}")


'''
No47
Ask the user to enter a number and then enter another number.
Add these two numbers together and then ask if they want to
add another number. if they enter "y", ask them to enter
another and keep adding numbers until they do not answer "y".
Once the loop has stooped, display the total.
'''
print("\n")
first_num = int(input("Enter a number: "))
total = first_num
confirm = "y"

while confirm == "y":
    new_number = int(input("Enter another number: "))
    total += new_number
    confirm = input("Do you want to add another number? y/n: ")
print(f"The total is: {total}")


'''
No48
Ask for the name of somebody the user wants to invite to a party.
After this, display the message "[name] has been invited" and
add 1 to the count. Then ask if they want to invite somebody
else.
Keep repeating this until they no longer want to invite
anyone else to the party and then display how many people they
have coming to the party.
'''
print("\n")
count = 0
new_invite = "y"
while new_invite == "y":
    name = input("Enter name of person you want to invite: ")
    print(f"{name} has now been invited.")
    count += 1
    new_invite = input("Do you want to invite someone else? y/n: ")
print(f"You have {count} people coming to the party.")


'''
No49
Create a variable called compnum and set the value to 50.
Ask the user to enter a number. While their guess is not
the same as the compnum value, tell them if their guess is
too low or too high and ask them to have another guess.
If they enter the same value as compnum, display the message
"Well done, you took [count] attempts".
'''
print("\n")
campnum = 50
guess = int(input("A game of guess. Guess a number: "))
count = 1
while guess != campnum:
    if guess < campnum:
        print("Too low.")
    else:
        print("Too high.")
    count += 1
    guess = int(input("Try another guess."))
print(f"Well done, you took {count} attempts.")


'''
No50
Ask the user to enter a number between 10 and 20. If they enter
a value under 10, display the message "Too low" and ask them
to try again. If they enter a value above 20, display the 
message "Too high" and ask them to try again. Keep repeating this
until they enter a value that is between 10 and 20 and then
display the message "Thank you".
'''
print("\n")
#SOLUTION 1
num = int(input("Enter a number between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Try again: "))
print("Thank you")


#SOLUTION 2
value = int(input("Enter a number between 10 and 20: "))
while value not in range(10, 21):
    if value < 10:
        print("Too low")
    else:
        print("Too high")
    value = int(input("Try again: "))
print("Thank you")


'''
No51
Using the song "10 green bottles", display the lines
"There are [num] green bottles hanging on the wall,
[num] green bottles hanging on the wall, and if 1 green
bottle should accidentally fall". Then ask the question
"how many green bottles will be hanging on the wall?"

If the user answers correctly, display the message
"There will be [num] green bottles hanging on the wall".
If they answer incorrectly, display the message "No, try again"
until they get it right. when the number of green bottles gets
down to 0, display the message "There are no more green bottles
hanging on the wall".
'''
print("\n")
num = 10
while num > 0:
    print(f"\nThere are {num} green bottles hanging on the wall.")
    print(f"{num} green bottles hanging on the wall.")
    print("And if 1 green bottle should accidentally fall.")
    num -= 1
    answer = int(input("How many green bottles will be hanging on the wall?: "))
    if answer == num:
        print(f"There are {num} green bottles hanging on the wall.")
    else:
        while answer != num:
            answer = int(input("No, try again.: "))
print("There are no more green bottles hanging on the wall.")