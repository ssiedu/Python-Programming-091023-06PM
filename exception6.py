try:
    print("In Try Block")
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))
    c=a/b

except:
    print("In Except Block")
    print("Some Error Occured")

else:
    print("in Else Block")
    print("Value of c :",c)

finally:
    print("In finally Block")
    print("Thank You")
