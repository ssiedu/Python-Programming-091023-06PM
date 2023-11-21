def Series():
    i=int(input("Enter Start Limit :"))
    num=int(input("Enter Stop Limit:"))
    sum=0
    while i<=num:
        print(i,end=" ")
        sum=sum+i
        i=i+1
    print()
    print("Sum of Series :",sum)


Series()
