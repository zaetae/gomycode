def max(a,b,c):
    M=a
    if(a>b)and(a>c):
        M=a
        return(a)
    if(b>c)and(b>a):
        M=b
        return(b)
    if(c>a)and(c>b):
        M=c
        return(c)
max(35,21,7)
print(max(35,21,7))
