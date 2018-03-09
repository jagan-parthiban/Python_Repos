def main():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    rarr = []

    for i in arr: 
        rarr.insert(0, i)
      
    for i in rarr:
        print(i, end=" ")    

if __name__ == '__main__':
    main()
    