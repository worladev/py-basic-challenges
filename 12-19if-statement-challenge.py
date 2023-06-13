### CHALLENGES AFTER LESSON ON [IF STATEMENTS] ###

# 12 Ask for two numbers. If the first one is larger than the
# second, display the second number first and then the first number
# otherwise show the first number first and then the second.
print("\n")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num1, num2)
else:
    print(num2, num1)


# 13 Ask the user to enter a number that is under 20. If they
# enter a number that is 20 or more, display the message
# "Too high", otherwise display "Thank you".
print("\n")
under_20 = int(input("Enter a number less than 20: "))
if under_20 >= 20:
    print("Too high.")
else:
    print("Thank you.")


# 14 Ask the user to enter a number between 10 and 20(inclusive).
# If they enter a number within this range, display the message
# "Thank you", otherwise display the message "Incorrect answer".
print("\n")
user_choice = int(input("Enter a number between 10 and 20: "))
if user_choice >= 10 and user_choice <= 20:
    print("Thank you.")
else:
    print("Incorrect answer.")


# 15 Ask the user to enter their favourite color. If they enter
# "red", "RED" or "Red" display the message "I like red too",
# otherwise display the message "I don't like [color], I prefer red".
print("\n")
fav_color = input("Enter your favourite color: ")
if fav_color.lower() == "red":
    print("I like red too.")
else:
    print("I don't like ", fav_color, "I prefer red")


# 16 Ask the use if it is raining and convert their answer
# to lower case so it doesn't matter what case they type
# it in. If they answer "yes", ask if it is windy. If they
# answer yes to this second question, display the answer 
# "It is too windy for an umbrella", otherwise display
# the message "Take an umbrella".  if they did not answer
# yes to the first question, display the answer.
# "Enjoy your day"
print("\n")
rain = input("Is it raining: ")
rain = str.lower(rain)
if rain == "yes":
    wind = input("Is it windy: ").lower()
    if wind == "yes":
        print("It is too windy for an unbrella.")
    else:
        print("Take an unbrella.")
else:
    print("Enjoy your day.")


# 17 Ask the user's age. If they are 18 or over, display the
# message "You can vote", if they are aged 17, display the
# message "You can learn to drive", if they are 16, display
# the message "You can buy a lottery ticket", if they are
# under 16, display the message "You can go Trick-or-Treating".
print("\n")
user_age = int(input("Enter your age.: "))
if user_age >=18:
    print("You can vote.")
elif user_age == 17:
    print("You can learn to drive")
elif user_age == 16:
    print("You can buy a lottery ticket.")
else:
    print("You can go Trick-or-Treating.")


# 18 Ask the user to enter a number. If it is under 10,
# display the message "Too low", if their number is between
# 10 and 20, display "Correct", otherwise display
# "Too high".
print("\n")
number = int(input("Enter a number: "))
if number < 10:
    print("Too low")
elif number >= 10 and number <= 20:
    print("Correct")
else:
    print("Too high")


# 19 Ask the user to enter 1, 2 or 3. If they enter a 1,
# display the message "Thank you", If they enter a 2,
# display "Well done", if they enter a 3, display "Correct".
# If they enter anything else, display "Error message".
print("\n")
choice = input("Enter 1, 2 or 3")
if choice == "1":
    print("Thank you")
elif choice == "2":
    print("Well done.")
elif choice == "3":
    print("Correct")
else:
    print("Error message")

