n1=eval(input("Enter First Number :"))#12
n2=eval(input("Enter Second number :"))#15

print("And :",(n1>n2 and n1==n2))#False
print("or  :",(n1!=n2 or n1<n2))#True
print("Not :",not(n1==n2))#True
print("And not :",not((n1<n2) and not(n1)))#True
print("Or not :",not(n1>n2 or n1==n2))#True
print("And or Not:",not(((n1<n2) and (n1!=n2)) or not(n1<n2)))#F
