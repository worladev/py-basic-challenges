### CHALLENGES AFTER LESSON ON [TUPLES, LISTS AND DICTIONARIES] ###

'''No69
Create a tuple containing the names of five countries and display
the whole tuple. Ask the user to enter one of the countries that
have been shown to them and then display the index number
(i.e. position in the list) of that item in the tuple.
'''
country_names = ("Ghana", "Nigeria", "Rwanda", "Tanzania", "Libya")
print("\n", country_names)
user_choice = input("Enter one of the country name: ")
user_choice = user_choice.capitalize()
print(f"{user_choice} is at index {country_names.index(user_choice)}")


'''No70
Add to program 069 to ask the user to enter a number and
display the country in that postition.
'''
country_names = ("Ghana", "Nigeria", "Rwanda", "Tanzania", "Libya")
print("\n", country_names)
user_choice = input("Enter one of the country name: ")
user_choice = user_choice.capitalize()
print(f"{user_choice} is at index {country_names.index(user_choice)}")
user_choice = int(input("Enter a number between 0 and 4: "))
print(country_names[user_choice])


'''No71
Create a list of two sports. Ask the user what their
favourite sport is and add this to the end of the
list. Sort the list and diplay it.
'''
sports = ["soccer", "basketball"]
sports.append(input("What is your favourite sport: "))
sports.sort()
print(sports)

'''No72
Create a list of six school subjects. Ask the user
which of these subjects they don't like. Delete
the subject they have chosen from the list before
you display the list again.
'''
subjects = ["ICT", "English", "Mathematics", "Biology", "Chemistry", "Programming"]
print(subjects)
dislike = input("Which of these subjects don't you like?: ")
dislike = dislike.capitalize()
rem = subjects.index(dislike)
del subjects[rem]
# subjects.remove(dislike)
print(subjects)


'''No73
Ask the user to enter four of their favourite foods
and store them in a dictionary so that they are indexed
with numbers starting from 1. Display the dictionary
in full, showing the index number and the item. Ask
them which they want to get rid of and remove it from
the list. Sort the remaining data and display the 
dictionary.
'''
again = 1
favourite_food = dict()
while again < 5:
    fav_food = input("\nEnter your favourite food: ")
    favourite_food[again] = fav_food
    again += 1
print(favourite_food)
rem = int(input("Which number do you want to remove?: "))
del favourite_food[rem]
print(sorted(favourite_food.values()))

'''No74
Enter a list of ten colors. Ask the user for a starting
number between 0 and 4 and an end number between
5 and 9. Display the list for those colors between
the start and end numbers the user input.
'''
colors = [
    "red", "orange", "blue",
    "green", "black", "violet",
    "purple", "maroon", "yellow",
    "white", "grey"
    ]
start = int(input("\nEnter a start number between 0 and 4: "))
stop = int(input("Enter an end number between 5 and 9: "))
if start in range(0, 5) and stop in range(5, 10):
    print(colors[start:stop])
else:
    print("Incorrect start or stop number.")


'''No75
Create a list of four three-digit numbers. Display
the list to the user, showing each item from the
list on a separate line. Ask the user to enter a
three-digit number. if the number they have typed
matches one in the list, display the position of that
number in the list, otherwise display the message
"That is not in the list"
'''
numbers = [333, 193, 267, 845]
for num in numbers:
    print(num)

user = int(input("\nEnter a three-digit number: "))
if user in numbers:
    print(numbers.index(user))
else:
    print("That is not in the list")


'''No76
Ask the user to enter the names of three people they
want to invite to a party and store them in a list.
After they have entered all three names, ask them if
they want to add another. If they do, allow them to
add more  names until they answer "no". When they
answer "no", display how many people they have invited
to the party.
'''

invite1 = input("\nInvite three people to a party: ")
invite2 = input("Invite three people to a party: ")
invite3 = input("Invite three people to a party: ")
invited = [invite1, invite2, invite3]

another = input("Do you want to invite more (y/n)?: ")
while another == 'y':
    invite_more = invited.append(input("Enter name to invite: "))
    another = input("Do you want to invite more (y/n)?: ")
print(f"You have invited {len(invited)} people to the party.")
    

'''No77
Change program 076 so that once the user has completed
their list of names, display the full list and ask them
to type in one of the names on the list. Display the
position of that name in the list. Ask the user if they
still want that person to come to the party. If they
answer "no", delete that entry from the list and display
the list again.
'''
invite1 = input("\nInvite three people to a party: ")
invite2 = input("Invite three people to a party: ")
invite3 = input("Invite three people to a party: ")
invited = [invite1, invite2, invite3]

more = True
while more:
    response = input("Do you want to invite more (y/n)?: ")
    if response == 'y':
        invite_more = input("Enter name to invite: ")
        invited.append(invite_more)
    elif response == 'n':
        print(f"Your invited list is\n{invited}")
        one_invitee =  input("Type one name in your list: ")
        print(f"{one_invitee} is at position {invited.index(one_invitee)}")
        stillcome = input(f"Do you still want to invite {one_invitee}?\n'y' or 'n': ")
        if stillcome == 'n':
            invited.remove(one_invitee)
            print(invited)
        else:
            print("Thank you")
        more = False

'''No78
Create a list containing the titles of four TV programmes
and display them on separate lines. Ask the user to enter
another show and a position they want it inserted into the
list. Display the list again, showing all five TV 
programmes in their new position.
'''
tv_programs = [
    "gija morning show",
    "the cantata",
    "children's world",
    "now or never",
    ]
for prog in tv_programs:
    print(prog)

another_show = input("\nEnter another TV program: ")
position = int(input("Enter the position to insert your show: "))
tv_programs.insert(position, another_show)

for prog in tv_programs:
    print(prog)


'''No79
Create an empty list called "nums", Ask the user to enter
numbers. After each number is entered, add it to the
end of the nums list and display the list. Once they have
entered three numbers, ask them if they still want the
last number they entered saved. If they say "no",
remove the last item from the list.
Display the list of numbers.
'''
nums = []

again = True
while again:
    user_num = int(input("\nEnter num: "))
    nums.append(user_num)
    print(nums)

    if len(nums) == 3:
        still_enter = input("Do you want to save the last number? (y/n): ")
        if still_enter == 'n':
            nums.remove(user_num)
        print(nums)
        again = False


