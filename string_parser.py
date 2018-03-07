#!/bin/python3

import sys

# def decomposer():

def main():
    n = int(input().strip())
    for i in range(1,n+1):
        sval = str(input().strip())
        length = len(sval)
        # print("lenght is : " , length)
        for j in range(0,length):
            if(j%2 == 0):
                print(sval[j], end="")
        print(" ", end="")
        for k in range(0,length):        
            if(k%2 == 1):
                print(sval[k], end="")
        print("")

if __name__ == '__main__':
    main()
    