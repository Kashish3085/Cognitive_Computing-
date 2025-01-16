#3 If-Else Statements

#3.1 Check if positive, negative or zero

n=float(input("Enter number: "))
if n > 0:
    print("The number",n,"is positive\n")
elif n < 0:
    print("The number",n,"is negative\n")
else:
    print("The number is zero\n")

#3.2 check if odd or even

num=int(input("Enter the number: "))
if num % 2 == 0:
    print("The number",num,"is even")
else:
    print("The number",num,"is odd")
