### CHALLENGES AFTER LESSON ON [STRINGS] ###

# 20 Ask the user to enter their first name and then display
# the length of their name.
firstname = input("Enter your first name: ")
length_of_name = len(firstname)
print("The length of your name is: ", length_of_name)


# 21 Ask the user to enter their first name then ask them
# to enter their surname. Join them together with a
# space between and display the name and the length of
# whole name
print("\n")
firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
fullname = f"{firstname} {surname}"
print(f"Your fullname is: {fullname}")
print(f"The length of your name is: {len(fullname)}")


# 22 Ask the user to enter their first name and surname in
# lower case. Change the case to title case and join them
# together. Display the finished result.
print("\n")
firstname = input("Enter your first name in lower case: ").title()
surname = input("Enter your surname in lower case: ").title()
firstname = firstname.title()
surname = surname.title()
fullname = f"{firstname} {surname}"
print(fullname)


# 23 Ask the user to type in the first line of a nursery rhyme
# and display the length of the string. Ask for a starting
# number and an ending number and then display just that section
# of the text (remember Python starts counting from 0 and not 1)
print("\n")
nursery_rhyme = input("Type the first line of any nursery rhyme: ")
length_of_rhyme =  len(nursery_rhyme)
print(f"Your rhyme has {length_of_rhyme} letters in it.")
start = int(input("Select a starting number: "))
end = int(input("Select an ending number: "))
part = nursery_rhyme[start:end]
print(part)


# 24 Ask the user to type in any word and display it in
# upper case
print("\n")
word = input("Type in any word of your choice: ")
print(word.upper())


# 25 Ask the user to enter their first name. If the lenght of
# their first name is under five characters, ask them to enter
# their surname and join them together (without a space) and
# display the name in upper case. If the length of the first
# name is five or more characters, display their first name
# in lower case.
print("\n")
name = input("Enter your first name: ")
if len(firstname) < 5:
    surname = input("Enter your surname: ")
    name = name + surname
    print(name.upper())
else:
    print(firstname.lower())


# 26 Pig Latin takes the first consonant of a word, moves
# it to the end of the word and adds on an "ay". If a word
# begins with a vowel you just add "way" to the end. For
# example, pig bexomes igpay, banana becomes ananabay, and
# aadvark becomes aadvarkway. Create a program that will
# ask the user to enter a word and change it into Pig Latin.
# Make sure the new word is displayed in lower case.
print("\n")

vowels = ["a", "e", "o", "i", "u"]
word = input("Enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != vowels:
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())
