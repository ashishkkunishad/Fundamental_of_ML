import numpy as np
a=np.array([[4,2],
            [1,3]])
w,v=np.linalg.eig(a)#eig function for finding eigen value and eigen vector
print("Eigen value:" ,w)
print("Eigen vector",v)