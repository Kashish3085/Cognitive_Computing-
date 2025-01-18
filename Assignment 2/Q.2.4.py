#4 Operation on sets 

#4.1 Union of sets 

A= {34, 56, 78, 90}
B= {78, 45, 90, 23}
unique= A.union(B)
print("Unique Score: ",unique)

#4.2 Intersection of Sets

common= A.intersection(B)
print("Common Scores: ",common)

#4.3 Symmetric Difference 

exclusive= A.symmetric_difference(B)
print("Exclusive Scores:",exclusive)

#4.4 Subset and Superset 

subset= A.issubset(B)
superset= B.issuperset(A)
print("Is A a subset of B ?: ",subset)
print("Is B a superset of A ?: ",superset)

#4.5 Remove a specific score

a= int(input("Enter score to be removed: "))
if a in A:
    A.remove(a)
    print(A)
else:
    print("Score",a,"is not present")
    