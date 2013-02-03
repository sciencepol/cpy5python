#q08_top2_scores.py
#Chua Ming Yu
#Date created: 29/1/2013
#Date modified: 03/2/2013

a=int(input("Enter number of students: "))
b=[]
c=[]
while a!=0:
    b.append(input("Please enter the student\"s name: "))
    c.append(input("Please enter the student\"s score: "))
    a=a-1
print("The student with the highest score is ",b[c.index(max(c))])
b.remove(b[c.index(max(c))])
c.remove(max(c))
print("The student with the second highest score is ",b[c.index(max(c))])
