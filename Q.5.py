#5 Data Structures

#5.1 Create List find largest and smallest 

a = [10, 30, 80, 20, 60]
l = max(a)
s = min(a)
print(a)
print("Largest number in the list:",l)
print("Smallest number in the list:",s,"\n")

#5.2 Create dictionary, retrieve value of a given key

dict= {1:"One", 2:"Two", 3:"Three"}
k = int(input("Enter the key to be retrieved:"))
if k in dict:
    print("Key found")
    print("value of key",k,":",dict[k])
else:
    print("Key not found")

#5.3 Sort list in ascending and descending

b=[10,45,67,23,6,88]
print("List before sorting: ",b)
asc= sorted(b)
print("Ascending Order: ",asc)
desc= sorted(b,reverse=True)
print("Descendin Order: ",desc)

#5.4 Merge two dictionaries

d1= {1:"One", 2:"Two", 3:"Three"}
d2= {4:"Four", 5:"Five", 6:"Six"}
d1.update(d2)
print("Merged Dictionary: ",d1)