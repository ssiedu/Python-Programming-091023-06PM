class Series:
    def getNum(self):
        self.num=int(input("Enter Any Number :"))
    def printSeries(self):
        for i in range(1,self.num+1):
            print(i,end=" ")


S=Series()
S.getNum()
S.printSeries()
