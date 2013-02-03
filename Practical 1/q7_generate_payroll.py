#generate payroll
#Chua Ming Yu
#Date created: 28/1/2013
#Date edited: 28/1/2013
#This program generates a person's payroll

a=str(input("What is your name: "))
b=float(input("How many hours do you work in a week: "))
c=float(input("How much do you earn per hour: "))
d=float(input("What is your CPF contribution rate: "))
print("Payroll statement for ",a)
print("Number of hours worked per week: ",b)
print("Hourly pay rate: $",c)
print("Gross pay= $",b*c)
e=b*c*d/100
print("CPF contribution at ",d,"% = $",e)
print("Net pay = ", b*c-e)
