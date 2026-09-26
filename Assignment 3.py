#Write a python program to check whether or not the triangle is a right angled triangle using functions
def inp():
    a=int(input("Enter length of first side"))
    b=int(input("Enter length of second side"))
    c=int(input("Enter length of third side"))
    return a,b,c
def triangle(a,b,c):
    if(a*a== b*b+c*c):
        print ("Right angled triangle")
    elif(b*b==a*a+c*c):
        print("Right angled triangle")
    elif(c*c==a*a+b*b):
        print("Right angled triangle")
    else:
        print("Not a right angled triangle")
a,b,c = inp()
triangle(a,b,c)