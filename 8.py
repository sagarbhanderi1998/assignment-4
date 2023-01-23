'''Write a python program to find the longest words. '''

n=int(input("Enter The Value of N:"))

f=open("data.txt","r")
s=f.read()
lst=s.split()

for i in lst:
    if(len(i)>n):
       print(i)





'''Write a python program to find the max and min words. '''

n=int(input("Enter The Max or min words Length of N:"))

f=open("data.txt","r")
s=f.read()
lst=s.split()

print(max(lst,key=len))
print(min(lst,key=len))








