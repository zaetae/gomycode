FirstNumber=int(input("Enter firstnumber"))
SecondNumber=int(input("Enter SecondNumber"))
ThirdNumber=int(input("Enter ThirdNumber"))
List=[FirstNumber,SecondNumber,ThirdNumber]
i=-1
while  i<len(List)-3 :
    i=i+1
    print(i)
    Value= List[i]*List[i+1]*List[i+2]
    print(Value)
