n=int(input())
if (n>=500):
    n=n/2
if (n<500) and (n>=200):
    n=n*(70/100)
else:
    n=n*(90/100)
print(n)