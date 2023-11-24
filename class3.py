class Area:
    def getRadius(self):
        self.r=eval(input("Enter Radius of circle :"))
    def calculate(self):
        self.area=3.14*self.r**2
    def display(self):
        print("Area of circle :",self.area)


A=Area()
A.getRadius()
A.calculate()
A.display()
