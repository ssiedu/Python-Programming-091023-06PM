char=input("Enter any character :")
match char.lower():
    case 'a'|'e'|'o'|'i'|'u':
        print("Vowel")
    case _:
        print("Consonant")
