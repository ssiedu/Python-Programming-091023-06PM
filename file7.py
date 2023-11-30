file=open("Myfile7.txt","w")
list1=[]
for i in range(5):
    name=input("Enter Name :")
    list1.append(name+"\n")

file.writelines(list1)
file.close()
