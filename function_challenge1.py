'''
NO 1
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


'''
NO 2
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


'''
NO 3
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

