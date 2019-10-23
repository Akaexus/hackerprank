import math
for i in range(int(input())):
    a, M = [int(x) for x in input().split()]
    print(math.ceil(math.log(M/a+1, 2)))