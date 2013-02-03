#q02_triangle.py
#Chua Ming Yu
#Date created: 29/1/2013
#Date modified: 29/1/2013

a=int(input("Side 1: "))
b=int(input("side 2: "))
c=int(input("Side 3: "))
if a+b>c and a+c>b and b+c>a:
    print("Perimeter = ", a+b+c)
else:
    print("Invalid triangle")
