# coding=utf-8
import re

mystring = "while(k!=0) /* Comentários */ if else // etaporra"

def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ), "", string)
    a = ""
    for i in string:
        b = a + i
        a = i
        if b == "//":
            string = string[:string.find("//")]



    return string

print(removeComments(mystring))