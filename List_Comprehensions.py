def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    iList = []
    for i in range (x+1):
        for j in range (y+1):
            for k in range (z+1):
                if (i+j+k != n):
                    iList.append([i,j,k])
                # print(iList)
        
    print(iList)    
if __name__ == '__main__':
    main()