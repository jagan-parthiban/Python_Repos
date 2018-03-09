if __name__ == '__main__':
    s = input()
#    if (s.isalnum()):
#        print("True")
#    else:
#        print("False")

    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0

    for i in s:
        if i.isalpha():
            flag1 = 1
        if i.isdigit():
            flag2 = 1
        if i.islower():
            flag3 = 1
        if i.isupper():
            flag4 = 1
        
    if (flag1 == 1 or flag2 == 1):
        print("True")
    else:
        print("False")
        
    if (flag1 == 1):
        print("True")
    else:
        print("False")

    if (flag2 == 1):
        print("True")
    else:
        print("False")

    if (flag3 == 1):
        print("True")
    else:
        print("False")

    if (flag4 == 1):
        print("True")
    else:
        print("False")


        
    