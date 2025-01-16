#6 Strings

#6.1 Count number of vowels

def count(s):
    c=0
    for char in s:
        if char in "aeiouAEIOU":
            c += 1
    return c

a= input("Enter the string: ")
print("Number of vowels: ",count(a),"\n")

#6.2 Reverse a string

def reverse(s):
    return s[::-1]

b= input("Enter the string: ")
print("The Reversed string is: ",reverse(b))

#6.3 Check if palindrome

def palindrome(s):
    if s == s[::-1]:
        print("the string is a palindrome")
    else:
        print("Not a palindrome")

p= input("Enter the string:")
palindrome(p)
