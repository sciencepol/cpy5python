#q1_sum_series1.py
#Author: Chua Ming Yu
#Date created: 21/2/2013
#Date edited: 21/2/2013

def sum_series(i):
    if i==0:
        return 0
    else:
        return 1/i+ sum_series(i-1)

