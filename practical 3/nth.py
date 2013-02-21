#q11_find_gcd.py
#Chua Ming Yu
#Date created: 03/02/2013
#Date modified: 03/2/2013
c=1
a=int(input("First number: "))
b=int(input("Second number: "))
while c!=0:
    c=a%b
    a=b
    b=c
print ("GCD of those 2 numbers is ",a)
