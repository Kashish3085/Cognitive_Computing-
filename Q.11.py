#11 Use Of Libraries

#11.1 Math Library

import math

n=int(input("Enter the number:"))
print(math.sqrt(n))

#11.2 datetime Library

import datetime

current= datetime.datetime.now()
print("current date and time: ",current)

#11.3 os Lbrary 

import os

files = os.listdir('.')
print("Files in the current directory:")
for file in files:
    print(file)



