class PosNeg:
    def getNum(self):
        self.num=int(input("Enter Any Number :"))
    def checkNum(self):
        if self.num>0:
            print("Positive Number ")
        else:
            print("Negative Number ")


E=PosNeg()
E.getNum()
E.checkNum()

