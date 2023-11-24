class Series:
    def getNum(self):
        self.num=int(input("Enter Any Number :"))
    def printSeries(self):
        i=1
        while(i<=self.num):
            if i%2!=0:
                print(i,end=" ")
            i=i+1


S=Series()
S.getNum()
S.printSeries()
