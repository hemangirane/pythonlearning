#Write a Python program which accepts
# the radius of a circle from the user and compute the area.

#option1
radius=float(input("Enter radius: "))
area=(3.14*(radius**2))
print(area)

#option2
radius=int(input("Enter radius: "))
print("{:F}".format(3.14*(pow(2,2))))
