#fahrenheit to celsius
#Chua Ming Yu
#Date created: 22/1/2013
#Date edited: 28/1/2013
#This program converts fahrenheit to celcius

print ("This program helps you to convert fahrenheit to celcius")
while True:
	try:
		x=float(input("Please input the number that you want to convert into celcius: ")
	except ValueError:
		print("Please input a number")
		continue
	y= (5/9) * (x - 32)
	print ("The temperature in celcius is ", y)