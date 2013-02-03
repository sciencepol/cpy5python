#Calculate cylinder volume
#Chua Ming Yu
#Date created: 22/1/2013
#Date edited: 28/1/2013
#This program converts miles to kilometres

while True:
    try:
        a=float(input("What is the number that you want to convert: "))
    except ValueError:
        print("ERROR")
        continue
    b=a/1.60934
    print("The distance is kilometres is ","{0:7.3f}".format(b),"km")
