#q2_sum_series2.py
#Author: Chua Ming Yu
#Date created: 21/2/2013
#Date edited: 21/2/2013

def sum_series2(i):
    if i==0:
        return 0
    else:
        return i/(2*i+1)+sum_series2(i-1)
