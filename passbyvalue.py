def Demo(d):
    #d[2]=100
    n=int(input("Enter any number :"))
    p=int(input("Enter position :"))
    d.insert(p,n)


L1=[1,2,3,4,5]
print("Before function call List is :")
print(L1)

Demo(L1)

print("After function call List is :")
print(L1)
