#7 File Handling

#7.1 Create a text file, write, read and print

f= open("Myfile.txt","w")
f.write("Hello!\n")
f.write("Nice to meet you!\n")
f.close()
f=open("Myfile.txt","r")
print(f.read())

#7.2 Append and print 

f=open("Myfile.txt","a")
f.write("How are you?\n")
f=open("Myfile.txt","r")
print(f.read())

#7.3 Count the number of lines 

f=open("Myfile.txt","r")
l= f.readlines()
count= len(l)
print("The number of lines in the file is: ",count)