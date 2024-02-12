import numpy as np#numpy-->> "numerical python" library for accessing different function
x=np.array([[1],[2],[3]])
print(x.shape,"\n")#
print(f'A 3-D vector:\n{x}')
print("\n")

y=np.array([[1],[2],[4]])
y.shape
np.add(y,x)

alpha=2
alpha*y
#np.multiply(alpha,y)
a,b=2,3
x,y=np.array([[2],[3]]),np.array([[4],[5]])
a*x + b*y

print(x.T@y)#for dot product of two vector x AND y 

#vector Norms
#1.Euclidean norm or L2 norm
x=np.array([[3],[4]])
print(np.linalg.norm(x,2))#2 becoz L2 norm
#2.Manhattan norm (L1 norm)
x=np.array([[3],[-4]])
print(np.linalg.norm(x,1))# 1becoz L1 norm
#3.Max norm (Infinity norm)
x=np.array([[3],[-4]])
print(np.linalg.norm(x,np.inf))

# for finding distance use Euclidean norm
x,y=np.array([[-2],[2]]),np.array([[4],[-3]])
distance=np.linalg.norm(x-y,2)
print(distance)

#Vecctor angles

x,y=np.array([[1],[-2]]),np.array([[5],[7]])

cos_theta=(x.T@y)/((np.linalg.norm(x,2))*(np.linalg.norm(y,2)))
print(cos_theta)

print(np.round(cos_theta,3))#for round of the output value,round function for round of
cos_inverse=np.arccos(cos_theta)#accos-->> for inverse 
print(cos_inverse)
degree=cos_inverse*((180)/np.pi)
print(degree)










