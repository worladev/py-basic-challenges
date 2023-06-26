### CHALLENGES AFTER LESSON ON [MORE ON STRING] ###

'''No80
Ask the user to enter their first name and then display the length
of their first name. Then ask for their surname and display the
length of their surname. Join their first name and surname together
with a space between and display the result. Finally, display the
length of their full name(including the space).
'''
first_name = input("\nEnter your firstname: ")
print(len(first_name))
last_name = input("Enter your surname: ")
print(len(last_name))
full_name = first_name + " " + last_name
print(full_name)
print(len(full_name))


'''No81
Ask the user to type in their favourite school subject. Display
it with "-" after each letter, e.g. S-p-a-n-i-s-h.
'''
fav_subj = input("\nEnter your favourite subject: ")
for letter in fav_subj:
    print(letter, end="-")


'''No82
Show the user a line of text from your favourite poem and ask for
a starting  and ending point. Display the characters between those
two points.
'''
poem = "\nThere are two little black birds."
print(poem)
start_point = int(input(f"Enter a starting point between 0 and {len(poem)}: "))
end_point = int(input(f"Enter an ending point between 0 and {len(poem)}: "))
print(poem[start_point:end_point])


'''No83
Ask the usr to type in a word in upper case. If they type it in
lower case, ask them to try again. Keep repeating this until they
type in a message all in uppercase.
'''

again = True
while again:
    word = input("\nEnter any word in uppercase: ")
    if word.isupper():
        print(word)
        again = False


'''No84
Ask the user to type in their postcode. Display the first two letters
in uppercase.
'''
post_code = input("\nEnter your postcode: ")
print(post_code[:2].upper())


'''No85
Ask the user to type in their name and then tell them how many vowels
are in their name.
'''
# name = input("\nEnter your name: ")
# vowels = "aeiou"
# count = 0
# for letter in vowels:
#     if letter in name:
#         count += 1
    
# print(count)


'''No86
Ask the user to enter a new password. Ask them to enter it again.
If the two passwords match, display "Thank you", If the letters
are correct but in the wrong case, display the message "They 
must be in the same case", otherwise, display the message 
"Incorrect".
'''
# CHECK AGAIN
# pass1 = input("Enter a password: ")
# pass2 = input("Enter a password again: ")
# if pass1 == pass2:
#     print("Thank you.")
# elif pass1.lower() == pass2.lower():
#     print("They must be the same case")
# else:
#     print("Incorrect")



'''No87
Ask the user to type in a word and then display it backwards
on separate lines. For instance, If they type in "Hello" it
should display as shown below:
o
l
l
e
H
'''
# word = input("\nEnter a word: ")
# index = len(word)
# while index > 0:
#     letter = word[index - 1]
#     print(letter)
#     index -= 1


