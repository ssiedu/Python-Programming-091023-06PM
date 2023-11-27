class Parent1:
    def getNum1(self):
        self.n1=eval(input("Enter First Number :"))


class Parent2:
    def getNum2(self):
        self.n2=eval(input("Enter Second Number :"))

class Parent3:
    def getNum3(self):
        self.n3=eval(input("Enter Second Number :"))

class Child(Parent1,Parent2,Parent3):
    def product(self):
        self.p=self.n1*self.n2*self.n3
    def display(self):
        print("Product of three number :",self.p)

C=Child()
C.getNum1()
C.getNum2()
C.getNum3()
C.product()
C.display()
        
