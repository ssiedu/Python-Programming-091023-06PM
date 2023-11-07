tuple1=()
#print(type(tuple1))
list1=list(tuple1)
#print(list1)
for i in range(5):
    var=int(input("Enter Number :"))
    list1.append(var)


print("Updated list :")
print(list1)
print("Tuple is :")
tuple1=tuple(list1)
print(tuple1)
