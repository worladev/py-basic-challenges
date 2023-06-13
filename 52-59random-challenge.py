### CHALLENGES AFTER LESSON ON [RANDOM] ###
import random

'''No52
Display a random integer between 1 and 100 inclusive.
'''
print("\n")
num = random.randint(1, 100)
print(num)

'''No53
Display a random fruit from a list of five fruits.
'''
print("\n")
fruits = ['mango', 'banana', 'orange', 'grape', 'pineapple']
rand_fruit = random.choice(fruits)
print(rand_fruit)

'''No54
Randomly choose either heads or tails("h" or "t"). Ask the user
to make their choice. If their choice is the same as the randomly
selected value, display the message "You win", otherwise
display the "Bad luck". At the end, tell the user if the 
computer selected heads or tails.
'''
head_or_tail = ['h', 't']
ht_choice = random.choice(head_or_tail)
user_choice = input("\nEnter 'h' or 't' to choose head or tail: ")
if user_choice == ht_choice:
    print("You won")
else:
    print("Bad luck")

print(f"Computer chose: {ht_choice}")

'''No55
Randomly choose a number between 1 and 5. Ask the user to pick
a number. If they guess correctly, display the message "Well done",
otherwise tell them if they are too high or too low and ask
them to pick a second number. If they guess correctly on their
second guess, display "Correct", otherwise display "You lose"..
'''
deal = random.randint(1, 5)
guess = int(input("\nGuess a number: "))
if guess == deal:
    print("Well done")
elif guess < deal:
    print("Too low")
    guess_again = int(input("Guess another number: "))
    if guess_again == deal:
        print("Correct")
    else:
        print("You lose")
elif guess > deal:
    print("Too high")
    guess_again = int(input("Guess another number: "))
    if guess_again == deal:
        print("Correct")
    else:
        print("You lose")


'''No56
Randomly pick a whole number between 1 and 10. Ask the user to
enter a number and keep entering numbers until they enter the
number that was randomly picked.
'''
deal = random.randint(1, 10)
guess =  int(input("\nEnter a number: "))
while deal != guess:
    guess = int(input("Guess again: "))
print("Correct.")


'''No57
Update program 056 so that it tells the user if they are too low
before they pick again.
'''
deal = random.randint(1, 10)
guess =  int(input("\nEnter a number: "))
while guess != deal:
    if guess < deal:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess again: "))
print("Correct.")


'''No58
Make a maths quiz that asks five questions by randomly generating
two whole numbers to make the question (e.g.[num1]+[num2]). Ask
the user to enter the answer. If they get it right add a point
to their score. At the end of the quiz, tell them how many
they got correct out of five.
'''
print("\n")
# SOLUTION 1
score = 0
for i in range(1, 6):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    answer = num1 + num2
    print(f"{num1} + {num2} = ")
    user_answer = int(input("Your answer: "))
    if user_answer == answer:
        score += 1
print(f"You scored {score} out of 5.")



# SOLUTION 2 using while loop
score = 0
while score < 5:
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    answer = num1 + num2
    print(f"{num1} + {num2} = ")
    user_answer = int(input("Your answer: "))
    if user_answer == answer:
        score += 1
print(f"You scored {score} out of 5.")


'''No59
Display five colours and ask the user to pick one.
If they pick the same as the program has chosen, say
"Well done", otherwise display a witty answer which involves
the correct colour, e.g. "I bet you are GREEN with envy or
"You are probably feeling BLUE right now". Ask them to guess
again; If they have still not got it right, keep giving them
the same clue and ask the user to enter a colour until they
guess it correctly
'''
color = random.choice(['blue', 'green', 'red', 'orange', 'purple'])
print("\nSelect 1 color from blue, green, red, orange, purple")
guess_again = True
while guess_again:
    guess = input("Pick one color: ")
    guess = guess.lower()
    if guess == color:
        print("Well done")
        guess_again = False
    else:
        if color == 'blue':
            print("You are probably feeling BLUE right now")
        elif color == 'green':
            print("As GREEN as a grass, you must be feeling.")
        elif color == 'red':
            print("You must be seeing some RED in the horizone.")
        elif color == 'orange':
            print("You must be feeling juicy ORANGE right now.")
        elif color == 'purple':
            print("How can PURPLE not be your blossom pinky?")


