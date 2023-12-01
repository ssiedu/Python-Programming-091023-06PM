try :
    a=10
    b=0
    c=a/b
    print("Value of c :",c)
except ZeroDivisionError:
    print("Zero Division Error")

except TypeError:
    print("Type Mismatch")
