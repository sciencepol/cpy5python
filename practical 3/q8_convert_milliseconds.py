#q8_convert_milliseconds.py
#Chua Ming Yu
#Date created: 20/2/2013
#Date edited: 20/2/2013


def convert_ms(n):
    a=n//1000
    b=a//60
    c=b//60
    print(c,":",b%60,":",a%60,sep='')

convert_ms(555550000)
