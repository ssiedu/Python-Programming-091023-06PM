import pickle
file=open("Myfile8","wb")
list1=[11,22,33,44,55]
pickle.dump(list1,file)
file.close()
file=open("Myfile8","rb")
data=pickle.load(file)
print(data)
file.close()
