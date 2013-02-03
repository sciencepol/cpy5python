#q03_determine_grade.py
#Chua Ming Yu
#Date created: 29/1/2013
#Date modified: 29/1/2013
while True:
    a=int(input("Please enter your score: "))
    if a>100:
        print("Invalid! Score must be between 0 - 100")
    elif a<=100 and a>=70:
        print("A")
    elif a>=60:
        print("B")
    elif a>=55:
        print("C")
    elif a>=50:
        print("D")
    elif a>=45:
        print("E")
    elif a>=35:
        print("S")
    elif a>=0:
        print("U")
    else:
        print("Invalid! Score must be between 0 - 100")
