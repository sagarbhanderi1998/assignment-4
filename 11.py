'''Write a Python program to write a list to a file.'''

#Given List.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


file=open('abc.txt', 'w')
for i in color:
    file.write('%s\n' % i)



print("Print Successfully")

file.close()
