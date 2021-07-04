import math as m
pi=m.pi
class circle:
    def __init__(self,xy_coord,r):
        self.xy_coord=xy_coord
        self.r=r
    def area(self):
        self.A= self.r*pi*2
        print(self.A)
    def perimeter(self):
        self.P= self.r*pi*2
        print(self.P)
    def isinside(self,xy):
        a=self.a=self.xy_coord[0]
        c=self.c=self.xy_coord[1]
        x=xy[0]
        y=xy[1]
        D=(((x-a)**2)+((y-c)**2))**0.5
        if (D==self.r):
            print("A belongs to the circle")
        elif (D<self.r):
            print("A is in the circle.")
        else:
            print("A doens't belong to the circle")
circle=circle([0,0],4)
circle.isinside([3,0])
circle.perimeter()
circle.area()
    
        