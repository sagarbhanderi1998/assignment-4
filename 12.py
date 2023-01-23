'''Write a Python program to copy the contents of a file to another file.'''

file1=open("data1.txt","r")
file2=open("copy.txt","w")

s=file1.read()
file2.write(s)

file1.close()
file2.close()
