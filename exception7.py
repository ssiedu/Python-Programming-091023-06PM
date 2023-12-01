try:
    num=int(input("Enter Any Number :"))
    assert num%2==0

except:
    print("Number is not Valid")

else:
    rec=1/num
    print("Reciprocal of a number :",rec)
