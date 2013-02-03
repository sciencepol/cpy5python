#q12_find_factors.py
#Chua Ming Yu
#Date created: 03/02/2013
#Date modified: 03/2/2013

a=int(input("Input a number: "))
i=2
while a!=0:
    if a%i==0:
        a=a/i
        print (i)
    else:
        i=i+1
