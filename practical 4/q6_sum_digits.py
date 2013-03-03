#q6_sum_digits.py
#Author: Chua Ming Yu
#Date created: 3/3/2013
#Date edited: 3/3/2013

def sum_digits(n):
    if n//10==0:
        return n
    else:
        return n%10+sum_digits(n//10)
    
