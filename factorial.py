#!/bin/python3

import sys

def factorial(n):
    x = 1
    for i in range(1,n+1):
        x = x * i
    return x
        

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
