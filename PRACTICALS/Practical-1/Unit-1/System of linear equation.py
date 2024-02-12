#system of linear equation
#x + 2y=8
#5x-3y=1
import numpy as np
import pandas as pd

A=np.array([[0,2],#1st row
           [1,4]])#2nd row
print("Matrix A: ",A)
print("\n------------------")
print("dimension of matrix A:",A.shape)
print("\n------------------")

B=np.array([[3,1],
            [-3,2]])
sum=A+B
print("\n------------------")

print("\nsum by A+B=",sum)
print("\n------------------")

print("\nSum by Add",np.add(A,B))#add fuction to add
print("\n------------------")

#matrix-scalar multiplication
alpha=2
mat_scalar_mul=alpha*(np.add(A,B))
print("\nmul of 2 into sum of A+B=",mat_scalar_mul)
print("\n------------------")

#matrix vector multiplication

#print("A@x: ",A@x)

#matrix matrix mul

print("\nA@B: ",A@B)

#matrix inverse

print("\n----------------------------")

C=np.array([[1,2,1],
            [4,4,5],
            [6,7,7]])
C_inverse=np.linalg.inv(C)
print("\ninverse",C_inverse)

print("\n----------------------------")

I=C_inverse@C
print("\nI=",np.round(I))

print("\n----------------------------")

#matrix transpose
print(C.shape)
print("\n----------------------------")
transpose_C=C.T
print("transpose_C=",C.T)
print(transpose_C.shape)
print("\n----------------------------")

#Hadamard product
E=F=np.array([[0,2],#1st row
           [1,4]])#2nd row
print("\nHadamard product of E and F:",E*F)

print("\n----------------------------")


#gaussian elimination method 
G=np.array([[1,3,5],
            [2,2,-1],
            [1,3,2]])
y=np.array([[-1],
            [1],
            [2]])
solution=np.linalg.solve(G,y)#solve func gives the solved augmented matrix's solution
print("\nsoluton: ",solution)

#A set of n lineraly independent col vectors with n elements forms a basis 