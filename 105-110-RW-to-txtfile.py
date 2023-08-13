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


