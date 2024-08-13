import math

length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

surface_area = 2 * (length * width + length  * height + height * width)

print("The surface area of the cuboid is: {:.2f}".format(surface_area))
