import numpy as np
array=np.array([[1,8,9,7],[4,8,3,1],[7,8,6,10]])
for i in range (array.shape[0]):
    #to loop through rows in array
    print(array[i].mean())
