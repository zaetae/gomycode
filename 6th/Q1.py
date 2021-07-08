import numpy as np
import array as arr
a=arr.array('i',[])
n=int(input("enter size of array"))
for i in range (0,n):
    elem=int(input("enter %d array element:" %(i+1)))
    a.append(elem)
for i in a:
    print(i,end=" ")
a_tolist=a.tolist()
print(a_tolist)
