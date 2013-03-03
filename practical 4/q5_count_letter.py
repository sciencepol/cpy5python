#q5_count_letter.py
#Author: Chua Ming Yu
#Date created: 3/3/2013
#Date edited: 3/3/2013

def count_letter(string, ch):
    if len(string)==1:
        return string==ch
    else:
        return (string[0]==ch)+count_letter(string[1:],ch)
    
string=input("Enter a string\n")
ch = input("Enter a character: ")
print(count_letter(string,ch))
