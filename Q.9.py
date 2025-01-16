#9 Random Numbers

#9.1 5 random numbers 

import random
for i in range(5):
    print(random.randint(1,100))

#9.2 check random number is prime 

def prime(n):
    if n <= 1:
        print("Not a prime number")
    for i in range(2,(n//2)+1):
        if (n % i)== 0:
            print(n,"Is n0t a prime number")
            break
        else:
            print(n,"Is a prime number")
            break

r= random.randint(1,100)
print("Random Number:",r)
prime(r)

#9.3 rolling a die

roll = random.randint(1, 6)
print("You rolled a:", roll)

#9.4 shuffle a list of numbers 

a= [1,2,3,4,5,6,7,8,9,10,11,12,13]
print("Original :",a)
random.shuffle(a)
print("New: ",a)

#9.5 select item 

b=["Cherry","mango","Peach"]
s= random.choice(b)
print("Random item: ",s)

#9.6 password of given length

import string
def pass_word(l):
    word= string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choice(word) for i in range(l))
    return password
g=int(input("Enter the length:"))
print("Generated Password:",pass_word(g))

#9.7 random card from a deck of 52

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = [rank + " of " + suit for rank in ranks for suit in suits]
random_card = random.choice(deck)
print("Randomly picked card:", random_card)