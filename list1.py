list1=[]
for i in range(5):
    num=int(input("Enter number :"))
    list1.append(num)


print("list is :")
print(list1)

n=int(input("Please Enter item do u want to delete ?:"))
list1.remove(n)

print("Updated List :")
print(list1)
