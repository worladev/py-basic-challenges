''' HACKERRANK PYTHON PROBLEMS '''

'''
PROBLEM STATEMENT 1: Given the participants' score sheet for your University Sports Day, you are required to
find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

INPUT FORMAT: The first line contains . The second line contains an array A[] of n integers each separated by
a space.

CONSTRAINTS:
    2 <= n <= 10
    -100 <= A[i] <= 100

OUTPUT FORMAT: Print the runner-up score.

SAMPLE INPUT
5
2 3 6 6 5
'''
# SOLUTION

# n = int(input())
# arr = map(int, n.split())
arr = [2, 3, 6, 6, 5]
    
arr_length = len(arr)
first = arr[0]
for i in range(1, arr_length):
    if arr[i] >= first:
        next = arr[i]
        first = next
    else:
        print(arr[i])