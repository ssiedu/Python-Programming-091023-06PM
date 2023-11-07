t1=(11,22,33,44,55,66)
#For LOOP

print("Tuple Is :")
for i in t1:
    print(i,end=" ")

print()
#Range

print("Tuple is :")
for i in range(len(t1)):
    print(t1[i],end=" ")

print()
#While LOOP
print("Tuple is :")
i=0;
while i<len(t1):
    print(t1[i],end=" ")
    i=i+1
