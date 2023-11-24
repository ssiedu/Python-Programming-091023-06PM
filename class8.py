class Largest:
    def getNum(self):
        self.num1=int(input("Enter First Number :"))
        self.num2=int(input("Enter Second Number :"))
    def checkNum(self):
        if self.num1>self.num2:
            print("Num1 is greater ",self.num1)
        else:
            print("Num2 is greater ",self.num2)


E=Largest()
E.getNum()
E.checkNum()

