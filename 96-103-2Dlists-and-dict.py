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
