#q7_find_largest.py
#Author: Chua Ming Yu
#Date created: 3/3/2013
#Date edited: 3/3/2013

def find_largest(alist):
    if len(alist)==1:
        return alist[0]
    else:
        if alist[0]>alist[1]:
            alist[1]=alist[0]
        return find_largest(alist[1:])
