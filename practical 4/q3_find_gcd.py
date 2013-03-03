#q3_find_gcd.py
#Author: Chua Ming Yu
#Date created: 22/2/2013
#Date edited: 22/2/2013

def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
