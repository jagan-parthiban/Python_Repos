def mutate_string(string, position, character):
    string = string[:position] + "k" + string[position+1:]
    return string

    # Method 2 
    # >>> string = "abracadabra"
    # >>> l = list(string)
    # >>> l[5] = 'k'
    # >>> string = ''.join(l)
    # >>> print string
    # abrackdabra

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)