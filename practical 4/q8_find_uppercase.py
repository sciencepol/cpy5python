#q8_find_uppercase.py
#Author: Chua Ming Yu
#Date created: 3/3/2013
#Date edited: 3/3/2013

def find_num_uppercase(string):
    if len(string)==(1):
        return (string[0].isupper())
    else:
        return (string[0].isupper())+find_num_uppercase(string[1:])
string=input('Please enter a word ')
print (int(find_num_uppercase(string)))
