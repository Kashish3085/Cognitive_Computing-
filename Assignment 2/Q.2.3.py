#3 Create list of 100 random numbers

#3.1 Count and print all odd numbers 

import random  

r= [random.randint(100,900)for x in range(100)]
print("List of random numbers:",r)
odd= [n for n in r if n % 2 != 0]
even= [n for n in r if n % 2 == 0]

def prime(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i== 0:
            return False
    return True

prim= [n for n in r if prime(n)]
print("Odd numbers:", odd)
print("Count of odd numbers: ",len(odd))

print("Even numbers:", even)
print("Count of even numbers: ",len(even))

print("Prime numbers:", prim)
print("Count of prime numbers: ",len(prim))

