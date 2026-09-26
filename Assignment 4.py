#Write a python program to create an array and perform addition of two matrices
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
print("A:")
print (a)
print("B:")
print(b)
print("Addition of A and B:")
print(np.add(a,b))
