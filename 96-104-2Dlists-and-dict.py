### CHALLENGES AFTER LESSON ON [2D LIST AND DICTIONARIES] ###

'''NO 96
Create the following using a simple 2D list using the standard
Python indexing
'''
list = [[2,5,8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)


'''NO 97
Using the 2D list from program 096, ask the user to select a row
and a column and display that value.
'''
list2 = [[2,5,8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("\nSelect a row: "))
col = int(input("Select a column: "))
print(list2[row][col])


'''NO 98
Using the 2D list from program 096 ask the user which row they would
like displayed and display just that row. Ask them to enter a new
value and add it to the end of the row and display the row again.
'''
list2 = [[2,5,8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
_row = int(input("\nWhich row would you like to see?: "))
print(list2[_row])
new_value = int(input("Enter new value to add: "))
list2[_row].append(new_value)
print(list2[_row])


'''NO 99
Change your previous program to ask the user which row they want
displayed. Display that row. Ask which column in that row they
want displayed and display the value that is held there. Ask the
user if they want to change the value. If they do, ask for a new
value and change the data. Finally, display the whole row again.
'''
list3 = [[2,5,8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
_row = int(input("\nWhich row would you like to see?: "))
print(list3[_row])
_col = int(input("Which column would you like to see in this row?: "))
print(list3[_row][_col])
change = input("Would you like to change this value? (y/n): ")
if change == 'y':
    change_value = int(input("Enter new value: "))
    list3[_row][_col] = change_value
print(list3[_row])


''' NO 100
Create the following using a 2D dictionary showing the sales each
person has made in the different geographical regions:
'''
sales = {
    "John": {"N":3056, "S":8463, "E":8441, "W":2694},
    "Tom": {"N":4832, "S":6786, "E":4737, "W":3612},
    "Anne": {"N":5239, "S":4802, "E":5820, "W":1859},
    "Fiona": {"N":3904, "S":3645, "E":8821, "W":2451}
}


'''NO 101
Using program 100, ask the user for a name and a region. Display the
relevant data. Ask the user for the name and region of data they
want to change and allow them to make the alteration to the sales
figure. Display the sales for all regions for the name they choose.
'''
sales2 = {
    "John": {"N":3056, "S":8463, "E":8441, "W":2694},
    "Tom": {"N":4832, "S":6786, "E":4737, "W":3612},
    "Anne": {"N":5239, "S":4802, "E":5820, "W":1859},
    "Fiona": {"N":3904, "S":3645, "E":8821, "W":2451}
}

name = input("\nEnter name: ")
region = input("\nEnter region: ")
name = name.title()
region = region.upper()
print(sales2[name][region])

new_data = int(input("Enter data to change: "))
sales2[name][region] = new_data

print(sales2[name])


'''NO 102
Ask the user to enter the name, age and shoe size for four people.
Ask for the name of one of the people in the list and display their
age and shoe size.
'''
people = dict()
for i in range(0, 4):
    name = input("\nEnter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    people[name] = {"age":age, "shoe size":shoe_size}

choice = input("Enter one of the name: ")
print(people[choice])


'''NO 103
Adapt program 102 to display the names and ages of all the people
in the list but do not show their shoe size.
'''
people = dict()
for i in range(0, 4):
    name = input("\nEnter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    people[name] = {"age":age, "shoe size":shoe_size}

for name in people:
    print(name, people[name]["age"])


'''NO 104
After gathering the four names, ages and shoe sizes, ask the user
to enter the name of the person they want to remove from the list.
Delete this row from the data and display the other rows on separate
lines.
'''

people = dict()
for i in range(0, 4):
    name = input("\nEnter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    people[name] = {"age":age, "shoe size":shoe_size}

rem = input("Enter name of person to remove: ")
del people[rem]

for item in people:
    print(item, people[item]["age"], people[item]["shoe size"])








