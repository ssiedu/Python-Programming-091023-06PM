class EvenOdd:
    def getNum(self):
        self.num=int(input("Enter Any Number :"))
    def checkNum(self):
        if self.num%2==0:
            print("Even Number ")
        else:
            print("Odd Number ")


E=EvenOdd()
E.getNum()
E.checkNum()

F=EvenOdd()
F.getNum()
F.checkNum()
