def main():
    print("Enter no of scores")
    n = int(input())
    print("enter the idividual scores")
    arr = map(int, input().split())

    flist = []
    for i in arr:
        flist.append(i)
    print(flist)

    high = max(flist)
    
    newflist = list(filter(lambda a: a != high, flist))
    newhigh = max(newflist)

    print(newhigh)

    # low = min(flist)
    # print("high", high) 
    # print("low", low)
     
    # fsec = flist[0]

    # for i in flist:
    #     if(i > low and i < high and i > fsec):
    #         fsec = i

    # print(fsec)

    
if __name__ == '__main__':
    main()