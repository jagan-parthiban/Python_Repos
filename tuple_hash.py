def main():
    n = int(input())
    lists = map(int, input().split())
    nlists = []
    for i in lists:
        nlists.append(i)
   
    tlp = tuple(nlists)
    hsh = hash(tlp)
    # print("List is ", lists)
    # print("List is ", nlists)
    # print(tlp)
    print(hsh)

if __name__ == '__main__':
    main()