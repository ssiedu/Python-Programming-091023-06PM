class Addition:
    def __init__(self):#Non para
        self.n1=10
        self.n2=20
    def __init__(self,a,b):#parameterized
        self.n1=a
        self.n2=b
    def Add(self):
        self.add=self.n1+self.n2
    def display(self):
        print("Addition is :",self.add)


#a=eval(input("Enter First Number :"))
#b=eval(input("Enter Second Number :"))

A=Addition(1,2)
A.Add()
A.display()
    
