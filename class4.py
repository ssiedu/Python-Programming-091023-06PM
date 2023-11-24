class Area:
    def getdata(self):
        self.l=eval(input("Enter length of rect :"))
        self.b=eval(input("Enter breadth of rect :"))
    def calculate(self):
        self.area=3.14*self.l*self.b
    def display(self):
        print("Area of circle :",self.area)


A=Area()
A.getdata()
A.calculate()
A.display()
