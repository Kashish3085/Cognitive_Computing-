#8 Exception Handling

#8.1, 8.2 Division by zero, invalid input

def divide(x,y):
    try:
        c= x/y
        print("result:",c,"\n")
    except ZeroDivisionError:
        print("Division by zero occured\n")
    except ValueError:
        print("Enter a valid input\n")

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
divide(a,b)

 #8.3 Use of finally

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Division by zero occured")
except ValueError:
    print("enter a valid number")
finally:
    print("Finally it's done")
