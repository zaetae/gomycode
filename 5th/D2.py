class Rectangle:
    
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        self.area=self.length*self.width
        print(self.area)
    def perimeter(self):
        self.perimeter=((self.length+self.width)*2)
        print(self.perimeter)
b=Rectangle(4,3)
b.perimeter()
b.area()

        
        
    