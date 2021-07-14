f=open("test.py")
n=int(input("number n of lines"))
lines=f.readlines()
last_lines = lines[-n:]
for i in last_lines:
    a=i.replace('n/','')
    print(a)
f.close()
