def VarLen(**d):
    print(d)
    for i,j in d.items():
        print(i,j)
    print(d['b'])
    

VarLen(a=10,b=20,c=30,d=40)
