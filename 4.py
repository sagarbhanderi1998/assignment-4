'''Write a Python program to read first n lines of a file'''
                    
'''Write a Python program to read last n lines of a file'''

file=open("data.txt","r")

n=int(input("Enter The No. of Lines: "))

for i in range(n):
    lst=file.readline()
    print(lst)
    
