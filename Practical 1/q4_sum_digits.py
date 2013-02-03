#summing_digits
#Chua Ming Yu
#Date created: 22/1/2013
#Date edited: 28/1/2013
#This program sums all the digits in an interger
while True:
    a=input("Please input a whole number between 0 and 1000: ")
    if a.isdigit()==True and int(a) < 1000 and int(a) > 0:
        print("The sum of the digits in a is", sum(map(int,str(a))))
    else:
        print("Error")
        continue
