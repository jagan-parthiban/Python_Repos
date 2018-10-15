def is_leap(year):
    
    if (year%4 != 0):
        leap = False
    elif (year%4 == 0 and year%100 != 0):
        leap = True
    elif (year%4 == 0 and year%100 == 0 and year%400 == 0):
        leap = True
    elif (year%4 == 0 and year%100 == 0 and year%400 != 0):
        leap = False      
    return leap

def main():
    year = int(input())
    print(is_leap(year))
    

if __name__ == '__main__':
    main()
 ## changed    time 8:40
