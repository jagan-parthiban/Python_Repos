#!/bin/python3
import sys

def bincount(n):
    x = '{0:b}'.format(n)
    lists = []
    flag = 0
    maxval = 0
    for i in x:
        lists.append(i)
    print(lists)
    for i in range(len(lists)):
        if ( i == 0 ):
            if ( lists[i] == "1"):
                flag = 1
                maxval = 1
        else:
            if ( lists[i] == "1" and flag == "0"):
                maxval = 1
                flag = 1
            elif ( lists[i] == "1" and flag == "1"):
                maxval = maxval + 1
                flag = 1
        print ("flag at each element in list", flag)
        print ("maxval at each element in list", maxval)
        
            
  
        # print("x of i value dealing is ", x[i])
        # if (i == 0):
        #     if (x[i] == "1"):
        #         start = 1
        #         flag = 1
        #         # print(start)
        # elif(i > 0):
        #     if (x[i] == "1" and flag == "1"):
        #         start = start + 1
        #         flag = 1
        #     elif (x[i] == "1" and flag == "0"):
        #         start = 1
        #         flag = 1
        # print("start value : ", start)

        
    return x
        

if __name__ == "__main__":
    n = int(input().strip())
    result = bincount(n)
    print(result)
