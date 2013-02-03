#Calculate cylinder volume
#Chua Ming Yu
#Date created: 22/1/2013
#Date edited: 28/1/2013
#This program calculates cylinder volume
import math
print("This program calculates cylinder volume")
while True:
	try:
		a=float(input("What is the diameter of the cylinder: "))
		b=float(input("What is the length of the cylinder: "))
	except ValueError:
		print("ERROR, TRY AGAIN")
		continue
	c=a/2
	d=c*c*math.pi
	e=d*b
	print("The volume of the cylinder is ", "{0:5.2f}".format(e), "unit cubed")