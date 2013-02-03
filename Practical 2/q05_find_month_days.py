#q05_find_month_days.py
#Chua Ming Yu
#Date created: 29/1/2013
#Date modified: 29/1/2013
a=str(input("Enter month: "))
c=int(input("Enter year: "))
b=a.lower()
if b=="september" or b=="april" or b=="june" or b=="november":
    print("There are 30 days in ",a,"",c)
elif b=="february":
    if c%4==0:
        print("There are 29 days in February ",c)
    else:
        print("There are 28 days in February ",c)
else:
    print("There are 31 days in ",a,"",c)
        
