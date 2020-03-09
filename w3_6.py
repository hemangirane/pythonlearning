# Write a Python program which accepts a sequence of
# comma-separated numbers from user and generate
# a list and a tuple with those numbers.

str_num = input("Enter numbers: ")
list_num = str_num.split(",")
print(list_num)

tup_num = tuple(list_num)
print(tup_num)

