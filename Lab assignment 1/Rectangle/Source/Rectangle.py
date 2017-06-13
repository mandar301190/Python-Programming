import math

number = input

while True:
	len = input("Length of rectangle: ")
	bre = input("Breadth of rectangle: ")

	length = int(len)
	breadth = int(bre)
	perimeter = (2*length) + (2*breadth)
	print("Perimeter of Rectangle =", perimeter)
