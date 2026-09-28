#Write a program to find the largest of three numbers
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))#input
if(a>b and a>c):#conditional statement 1
    print(a," is the largest")
elif (b>a and b>c):#conditional statement 2
    print(b," is the largest")
else:
    print(c," is the largest")#end of else