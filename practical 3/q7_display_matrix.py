#q7_display_matrix.py
#Chua Ming Yu
#Date created: 20/2/2013
#Date edited: 20/2/2013

import random
def print_matrix(n):
    m=n
    a=n
    while m!=0:
        n=a
        while n!=0:
            print (random.randint(0,1),end=" ")
            n-=1
        print()
        m-=1
        
print_matrix(6)
