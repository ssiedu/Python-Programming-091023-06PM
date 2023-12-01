try:
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))
    c=a+b
    print("Add is :",c)

except ZeroDivisionError:
    print("Divide by Zero Not Allowed")

except:
    print("Some Error Occured")
