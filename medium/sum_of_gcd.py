import sys

n = int(input())


def gcd(a, b):
    while(b):
        r = a % b
        a = b
        b = r
    return a


for i in range(n):
    sumOfGcd = 0
    integers = [int(x) for x in input().split()][1:]
    for i in range(len(integers)):
        for j in range(len(integers)):
            if j != i:
                # print(integers[i], integers[j], '->', gcd(integers[i], integers[j]))
                sumOfGcd += gcd(integers[i], integers[j])
    print(int(sumOfGcd/2))


