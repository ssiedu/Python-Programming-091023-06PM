file=open("Myfile5.txt","a")
n=int(input("How Many Students record do u want to enter:")) 
for i in range(n):
    name=input("Enter Name :")
    rn=int(input("Enter Roll Number :"))
    per = eval(input("Enter percentage :"))
    data=name+"\t"+str(rn)+"\t"+str(per)+"\n"
    file.write(data)
file.close()
