#q2_display_pattern.py
#Chua Ming Yu
#Date created: 21/2/2013
#Date edited: 21/2/2013

def display_pattern(n):
    a=1
    b=1
    
    while n!=0:
        loop_counter=0
        a=b
        while loop_counter<n:
            print (" ",end=" ")
            loop_counter+=1
        while a!=0:
            print(a,end=" ")
            a-=1
        print()
        n-=1
        b+=1


display_pattern(10)
        
