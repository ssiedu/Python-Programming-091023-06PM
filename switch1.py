ch=int(input("Enter Any number in between 1-5:"))
match ch:
    case 1:
        print("C Program")
    case 2:
        print("CPP")
    case 3:
        print("Python")
    case 4:
        print("Java")
    case 5:
        print("Ruby")
    case _:
        print("Invalid Choice")
