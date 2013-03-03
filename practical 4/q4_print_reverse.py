#q4_print_reverse.py
#Author: Chua Ming Yu
#Date created: 22/2/2013
#Date edited: 3/3/2013

def reverse(n):
    if n//10==0:
        return n*10
    else:
        
        return (n%10)*(10**len(str(n)))+ reverse(n//10)
def reverse_int(n):
    return reverse(n)//10
