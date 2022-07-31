
#Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.
with open("file1.txt") as file1:
    file_data1 = file1.readlines()

with open("file2.txt") as file2:
    file_data2 = file2.readlines()

result = [int(num) for num in file_data1 if num in file_data2]


print(result)


