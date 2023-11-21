def Largest(n1,n2):    
    if n1>n2:
        print("{} is greater than {}".format(n1,n2))
    elif n2>n1:
        print("{} is greater than {}".format(n2,n1))
    else:
        print("Both Are Equal")

n1=int(input("Enter First Number :"))
n2=int(input("Enter Second Number :"))
Largest(n1,n2)
        
