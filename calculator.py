while True:    
    n1=eval(input("Enter First number :"))
    ch=input("Enter operator(+,-,*,/) :")
    n2=eval(input("Enter Second Number :"))
    match ch:
        case '+':
            print("{} + {} = {}".format(n1,n2,n1+n2))
        case '-':
            print("{} - {} = {}".format(n1,n2,n1-n2))
        case '*':
            print("{} * {} = {}".format(n1,n2,n1*n2))
        case '/':
            print("{} / {} = {}".format(n1,n2,n1/n2))
        case _:
            print("Please Enter valid choice")
    uc=input('''Do u want to Continue :
1.Yes('y')
2.No('N')
''')
    if uc.lower()=='y' or uc=='1':
        continue;
    else:
        break;
