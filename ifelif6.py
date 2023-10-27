AN=int(input("Enter Any Ascii Number:"))
if AN>=65 and AN<=90:
    print("Upper Case",chr(AN))
elif AN>=97 and AN<=122:
    print("Lower case",chr(AN))
else:
    print("Digit")
