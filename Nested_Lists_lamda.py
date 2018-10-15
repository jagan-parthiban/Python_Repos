def main():
    print("Please Enter No of Students")
    cand_no = int(input())
    #two-dimentional array
    myList = [[0 for x in range(2)] for y in range(cand_no)] 
    print(myList)
    for i in range(cand_no):
        print("Candidate No : ", i)
        print("Please Enter Candidate Name : ") 
        name = input()
        myList[i][0] = name
        print("please enter Candidate score : ")
        score = float(input())
        myList[i][1] = score

    #myList = [['jagan', 45.09], ['jp', 45.09], ['jack', 35.50], ['wolf', 86.35]]
    print("My List ", myList)

    low = []
    low = min(myList, key=lambda x: x[1])
    print(low[1])

    newmyList = list(filter(lambda a: a[1] != low[1], myList))
    print("New My List : ", newmyList)

    newlow = []
    newlow = min(newmyList, key=lambda x: x[1])
    print(newlow[1])

    verynewmyList = list(filter(lambda x: x[1] == newlow[1], newmyList))
    print("Very New My List : ", verynewmyList)

    namelist = []
    for i in verynewmyList:
        namelist.append(i[0])

    print(namelist)

    for i in sorted(namelist):
        print(i)
   
    
if __name__ == '__main__':
    main()

## Check Time 4:44 PM