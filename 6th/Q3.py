import numpy as np
x=int(input("enter a number"))
array=np.array([[1,3,8,9,4],[5,2,7,6,10]])
a=array[array>x]
print(a , "is higher than" , x)

