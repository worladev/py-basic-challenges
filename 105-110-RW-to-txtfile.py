### CHALLENGES AFTER LESSON ON [READING AND WRITING TO TEXT FILE] ###

# with open('txtFiles/myfile.txt', mode='r') as meta_file:
#     worla = meta_file.readline()
#     print(worla)


'''No 105
Write a new file called “Numbers.txt”. Add five numbers to the document which are stored on the
same line and only separated by a comma. Once you have run the program, look in the location where
your program is stored and you should see that the file has been created. The easiest way to view
the contents of the new text file on a Windows system is to read it using Notepad.
'''
with open('txtFiles/Numbers.txt', mode='w') as challenge_file:
    file1 = challenge_file.write('4,6,8,10,12')


'''No 106
Create a new file called “Names.txt”. Add five names to the document, which are stored on separate lines.
Once you have run the program, look in the location where your program is stored and check that the file
has been created properly. 
'''
with open('txtFiles/Names.txt', mode='w') as challenge_file:
    file2 = challenge_file.write('James\n')
    file2 = challenge_file.write('Michael\n')
    file2 = challenge_file.write('Jane\n')
    file2 = challenge_file.write('Lisa\n')
    file2 = challenge_file.write('Riley\n')


'''No 107
Open the Names.txt file and display the data in Python.
'''
with open('txtFiles/Names.txt', mode='r') as challenge_file:
    file3 = challenge_file.read()
    print(file3)


'''No 108
Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and display
the entire file. 
'''
new_name = input('Enter a new name: ')
with open('txtFiles/Names.txt', mode='a') as challenge_file:
    file4 = challenge_file.write(new_name)

with open('txtFiles/Names.txt', mode='r') as challenge_file:
    file4 = challenge_file.read()
    print(file4)


'''No 109
Display the following menu to the user:
    1) Create a new file
    2) Display the file
    3) Add anew item to the file
    Make a selection 1, 2 or 3:

Ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a
suitable error message.

If they select 1, ask the user to enter a school subject and save it to a new
file called “Subject.txt”.
It should overwrite any existing file with a new file.

If they select 2, display the contents of the “Subject.txt” file.

If they select 3, ask the user to enter a new subject and save it to the file and then display
the entire contents of the file. Run the program several times to test the options.
'''
print('''
1) Create a new file
2) Display the file
3) Add a new item to the file''')
choice = int(input("\nMake a selection 1, 2 or 3: "))

if choice == 1:
    subject = input("Enter a school subject: ")
    with open('txtFiles/Subject.txt', mode='w') as challenge_file:
        file5 = challenge_file.write(subject)
elif choice == 2:
    with open('txtFiles/Subject.txt', mode='r') as challenge_file:
        file5 = challenge_file.read()
        print(file5)
elif choice == 3:
    new_subject = input("Enter a school subject: ")
    with open('txtFiles/Subject.txt', mode='a') as challenge_file:
        file5 = challenge_file.write(f"{new_subject}\n")
    
    with open('txtFiles/Subject.txt', mode='r') as challenge_file:
        file5 = challenge_file.read()
        print(file5)
else:
    print("Invalid choice.")


'''No 110
Using the Names.txt file you created earlier, display the list of names in Python. Ask the user
to type in one of the names and then save all the names except the one they entered into a new
file called Names2.txt. 
'''
# SOLUTION 1 --> Using with open method
with open("txtFiles/Names.txt", mode='r') as challenge_file:
    print(challenge_file.read())

with open('txtFiles/Names.txt', mode='r') as challenge_file:
  select = input('Enter a name from the list: ')
  select = select + '\n'
  for row in challenge_file:
     if row != select:
        with open('txtFiles/Names2.txt', mode='a') as challenge_file:
           new_record = row
           challenge_file.write(new_record)


# SOLUTION 2
file = open('txtFiles/Names.txt', mode='r')
print(file.read())
file.close()

file = open('txtFiles/Names.txt', mode='r')
select = input('Enter a name from the list: ')
select = select + '\n'
for row in file:
    if row != select:
        file = open('txtFiles/Names2.txt', mode='a')
        new_record = row
        file.write(new_record)
        file.close()
file.close()
