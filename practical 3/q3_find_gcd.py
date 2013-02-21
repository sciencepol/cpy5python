#q3_find_gcd.py
#Chua Ming Yu
#Date created: 18/2/2013
#Date edited: 18/2/2013
def gcd(m, n):
    c=1
    while c!=0:
        c=m%n
        m=n
        n=c
    print ("GCD of those 2 numbers is ",m)

gcd(2,3)
