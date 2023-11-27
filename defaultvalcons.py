class Addition:
    def __init__(self,a=0,b=0):
        self.n1=a
        self.n2=b
    def Add(self):
        self.add=self.n1+self.n2
    def display(self):
        print("Addition is :",self.add)


a=eval(input("Enter First Number :"))
b=eval(input("Enter Second Number :"))

A=Addition(a,b)
A.Add()
A.display()
    
