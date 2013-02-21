#q6_determine_prime.py
#Chua Ming Yu
#Date created: 20/2/2013
#Date edited: 20/2/2013

from math import sqrt

def is_prime(n):
    i=2
    while i<sqrt(n):
        if n%i==0:
            return False
        else:
            i+=1
    return True


loop_counter=0

n=2
while True:
    while is_prime(n)==True and loop_counter<1000:
        if loop_counter%10==0:
            print()

            
        print ("{0:<5.0f}".format(n),end='')
        n+=1
        loop_counter+=1
            
    else:
        n+=1
