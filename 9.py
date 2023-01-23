'''Write a Python program to count the number of lines in a text file.'''

file=open("data1.txt","r")
count=0
# store the string in content

content=file.read()
list=content.split('\n')

print(list)

for i in list:
    if i:
        count+=1
print("Number of Line in File Are:",count)

file.close()
