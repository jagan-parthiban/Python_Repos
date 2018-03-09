def perform(lists, oper):
    temp = oper.split()
    print(temp)
    
    flag = 0
    if ('insert' in temp):
        new_list = lists.insert(int(temp[1]), int(temp[2]))
    elif('print' in temp):
        flag = 1
        new_list = lists
    elif('remove' in temp):
        new_list = lists.remove(int(temp[1]))
    elif('append' in temp):
        new_list = lists.append(int(temp[1]))
    elif('sort' in temp):
        new_list = lists.sort()
    elif('pop' in temp):
        new_list = lists.pop()
    elif('reverse' in temp):
        new_list = lists.reverse()
    return new_list,flag
    

def main():
    n = int(input().strip())
    lists = []
    for line in range(n):
        oper = input()
        outt, flagz = perform(lists, oper)
        if (flagz == 1):
            print("Its a print statement", outt)


    print("List is ", outt)
if __name__ == '__main__':
    main()
    