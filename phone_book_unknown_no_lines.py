# from sys import stdin

def find_number(dict, line):
    if line in dict:
        connum = dict[line]
    else:
        connum = 0
    return connum

def main():
    n = int(input().strip())
    dict = {}
    for i in range(n):
        name = input().split(" ")
        dict[name[0]] = name[1]
    inputs = []
   
    # sentinel = ''
    # for line in iter(input, sentinel):
    #     inputs.append(line)

    
    while True:
        try:
            line = input()
            if line:
                inputs.append(line)
            else:
                break
        except:
            break
    
    for i in inputs:
        valz = find_number(dict, i)
        if (valz != 0):
            print(i + "=" + valz)
        else:
            print("Not found")
 
if __name__ == '__main__':
    main()
    