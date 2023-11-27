import math
class Parent:
    def __init__(self,r):
        #self.r=eval(input("Enter Radius of circle :"))
        self.r=r


class Child(Parent):
    def calArea(self):
        self.area=math.pi*self.r*self.r
        print("Area of circle :%.2f"%self.area)



C=Child(3)
#C.getdata()
C.calArea()
