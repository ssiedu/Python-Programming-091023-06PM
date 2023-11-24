class SI:
    def getdata(self):
        self.p=eval(input("Enter principle amount :"))
        self.r=eval(input("Enter rate of inetrest :"))
        self.t=eval(input("Enter time in year :"))
    def calculate(self):
        self.si=(self.p*self.r*self.t)/100
        self.total=self.p+self.si
    def display(self):
        print("simple interest :",self.si)
        print("Total Amount :",self.total)


A=SI()
A.getdata()
A.calculate()
A.display()
