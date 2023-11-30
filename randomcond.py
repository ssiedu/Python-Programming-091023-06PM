import random
while True:
    com=random.randint(1,5)
    user=int(input("Enter any number :"))
    if (com>user):
        print("Computer Number :",com)
        print("Your Number is Smallest Number")
    elif(user>com):
        print("Computer Number :",com)
        print("Your Number is largest Number ")
    else:
        print("Computer Number :",com)
        print("Both are Equal")
    uc=int(input('''do u want to continue -
1.Yes
2.No
'''))
    if uc==1:
        continue;
    else:
        print("Thank You")
        break;
