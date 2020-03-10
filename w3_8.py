# Write a Python program to display
# the first and last colors from the following list.

color = input("Enter colors: ")
colorsplit = color.split(",")
colorlist = list(colorsplit)
print(colorlist[0], colorlist[-1])
