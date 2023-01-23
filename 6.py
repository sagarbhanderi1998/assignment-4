'''Write a Python program to read a file line by line and store it into a list'''

with open("data.txt") as f:
    content_list = f.readlines()

# print the list
print("Given List is :" ,content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print("New List is :" ,content_list)


