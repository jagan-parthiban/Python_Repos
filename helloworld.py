def man():
    cand_no = int(input())
    myList = [[0 for x in range(2)] for y in range(cand_no)] 
    for i in range(cand_no):
        name = input()
        myList[i][0] = name
        score = float(input())
        myList[i][1] = score

    low = []
    low = min(myList, key=lambda x: x[1])

    newmyList = list(filter(lambda a: a[1] != low[1], myList))

    newlow = []
    newlow = min(newmyList, key=lambda x: x[1])

    verynewmyList = list(filter(lambda x: x[1] == newlow[1], newmyList))

    namelist = []
    for i in verynewmyList:
        namelist.append(i[0])

    for i in sorted(namelist):
        print(i)
   
    
if __name__ == '__main__':
    main()