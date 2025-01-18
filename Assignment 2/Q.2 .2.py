#2 Tuples

#2.1 Highest score with index

T=(45,89.5,76,45.4,89,92,58,45)
print(T)
print("Highet score: ",max(T))

#2.2 Lowest score and count 

print(min(T))
print("Number of time low score occured: ",T.count(min(T)))

#2.3 Reverse and return as list

t= T[::-1]
print("Reversed Tuple:",t)
print("Reversed List: ",list(t))

#2.4 check if score exists and it's first occurence

a=int(input("Enter the score to be searched: "))
if a in T:
    i=T.index(a)
    print("Score",a," is found at index: ",i)
else:
    print("Score",a,"is not present")