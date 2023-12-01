try:
    num=int(input("Enter Number Upto 100 : "))
    if num>100:
        raise ValueError

except:
    print("Value is Out of range ")

else:
    print("Number is in Range")
    if num%2==0:
        print("Even")
    else:
        print("Odd")
