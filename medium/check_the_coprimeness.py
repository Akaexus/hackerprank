import math

t = int(input())

def gcd(a, b):
    while(b):
        r = a % b
        a = b
        b = r
    return a

def findCoprime(a):
    indices = range(1, math.floor(a/2) + 1)[::-1]
    for index in indices:
        if gcd(index, a) == 1:
            return index

for i in range(t):
    n = int(input())
    print(findCoprime(n))
