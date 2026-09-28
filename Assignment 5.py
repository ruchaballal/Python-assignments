#Write a python program to check that a string contains only a certain set of characters (in this case a-z,A-Z,0-9)
import re
a=input(" Enter a string")
txt=re.findall("[A-z]",a)
x=re.findall("[0-9]",a)
print("A-Z and a-z", txt)
print("0-9",x)
