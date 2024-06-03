#Write a Python program that checks if two input strings are anagrams (contain the same characters in different orders)

def anagram(n1,n2):
    if (sorted(n1)==sorted(n2)):
        print("This is an anagram")
    else:
        print("This is not an anagram")

n1 = input("Please enter first word : ")
n2 = input("Please enter second word : ")

anagram(n1,n2)



