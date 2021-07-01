import math
L1=[]
L2=[]
a=int(input("a")) #number of elements of L1
for i in range (a):
    element =input("elements")
    L1.append(int(element)) #fill the first list with the numbers of H
    
def calculate():
    for i in range (len(L1)):
        L2.append(math.floor((10*L1[i]/3)**0.5)) #to fill the second list
    print(L2)
calculate()