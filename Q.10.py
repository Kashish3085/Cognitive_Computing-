#10 Command Line Arguments

#10.1 accept ,add and print 

import sys
if len(sys.argv) != 3:
    print("Please provide two numbers as command-line arguments")
else:
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        sum = n1 + n2
        print("The sum:",sum)
    except ValueError:
        print("Please provide valid numbers")

#10.2 Print length

if len(sys.argv) != 2:
    print("Please provide a string")
else:
    s = sys.argv[1]
    print("The length of the string ",s,"is:",len(s))
