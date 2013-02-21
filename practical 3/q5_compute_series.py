#q5_compute_series.py
#Chua Ming Yu
#Date created: 20/2/2013
#Date edited: 20/2/2013

def m(i):
    a=0
    while i>0:
        a+=(4*((1/(2*i+1))-(1/(2*i-1))))
        i=i-2
    return (-a)
i=1
while i<20:
    print ("{0:<3.0f}{1:.11f}".format(i,m(i)))
    i+=2
