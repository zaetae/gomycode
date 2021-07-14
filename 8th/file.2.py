f= open("test.py",'r')
n=int(input("number of lines"))
i=0
for i in range (0,n):
    f_content=f.readline()
    print(f_content)
f.close()
    
    
    
