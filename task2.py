'''
Write a Python program that checks whether a given string is a palindrome (reads the same forwards and backwards). Ignore case and non-alphanumeric characters.
Concepts Covered: Strings, Control Flow
'''

#Method 1

'''
value = input("Please enter a word : ")
value = value.lower()

if value == value[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

'''

#Method 2

def palindrome(n):
    n = n.lower()
    return n == n[::-1]

word = input("Please enter a word : ")

if palindrome(word):
    print("This is a palindrome")
else:
    print("This is not a palindrome")

