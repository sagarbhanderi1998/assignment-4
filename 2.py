'''Write a Python program to read an entire text file'''

f=open("data.txt","r")

lst=f.readlines()

for i in lst:

    print(i)
f.close()

