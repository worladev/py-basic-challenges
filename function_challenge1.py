from collections import Counter
from string import punctuation

'''NO 1
Write a function called matches that takes two strings as arguments and returns how many matches there
are between the strings. 
A match is where the two strings have the same character at the same index. For instance, 
'python' and 'path' match in the first, third, and fourth characters, so the function should return 3
'''
def matches(str1, str2):
    _match = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                _match = _match + str1[i]
    return _match, len(_match)

print(matches("python", "path"))


'''NO 2
Write a function called one_away that takes two strings and returns True
if the strings are of the same length and differ in exactly one letter,
like bike/hike or water/wafer.
'''
def one_way(str1, str2):
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return True
            else:
                return False
    else:
        return f"Words are not the same length."
    
print(one_way("bike", "hike"))


'''NO 3
- Write a function called first_diff that is given two strings and returns the first
location in which the strings differ.
If the strings are identical, it should return -1.
'''
def first_diff(str1, str2):
    _min = min(len(str1), len(str2))
    for i in range(_min):
        if str1[i] != str2[i]:
            return i
    
    if str1 == str2:
        return -1

print(first_diff("hoke", "hike"))


'''NO 4
Implement a function called duplicate_count that takes a
string as input and returns the count of characters that
appear more than once in the string. The count should be
case-insensitive.
'''
# SOLUTION 1
def duplicate_count(str):
    for punc in punctuation:
        word = str.replace(punc, "")
    
    char_count = Counter(word)

    count = 0
    for value in char_count.values():
        if value > 1:
            count += 1
    return count

print(duplicate_count("function"))
print(duplicate_count("This is a sentence string."))





#SOLUTION 2
def duplicate_count(str):
    str = str.lower()  # Convert string to lowercase
    char_count = {}  # Dictionary to store character counts

#   Count the occurrences of each character in the string
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
        # print(char_count)


#   Counting the characters that appear more than once    
    count = 0
    # for key, value in char_count.items():
    #     if key > 1:
    #         count += 1

    for value in char_count.values():
        if value > 1:
            count += 1
    return count

print(duplicate_count("functions now"))
print(duplicate_count("This is a sentence string."))