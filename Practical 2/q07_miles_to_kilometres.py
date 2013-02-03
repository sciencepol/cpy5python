#q07_miles_to_kilometres.py
#Chua Ming Yu
#Date created: 29/1/2013
#Date modified: 29/1/2013
print("Miles Kilometres Kilomotres Miles")
for i in range(1,11):
    print("{0:<2.0f}".format(i),"{0:2}".format(""),"{0:<6.3f}".format(i*1.609),"{0:2}".format(""),"{0:3}".format(15+i*5),"{0:6}".format(""),"{0:7.3f}".format((15+i*5)/1.609))

