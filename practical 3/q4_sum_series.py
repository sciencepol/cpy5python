#q4_sum_series.py
#Chua Ming Yu
#Date created: 18/2/2013
#Date edited: 19/2/2013

def m_series(i):
    a=0
    while i!=0:
        a+=i/(i+1)
        i=i-1

    return a
i=1
while i!=21:
    print("{0:<3.0f} {1:5.4f}".format(i, m_series(i)))
    i=i+1
