import math

notPrimes = set([])

for i in range(2, math.floor(math.sqrt(100000)) + 1):
    notPrimes.update(list(range(i*2, 100000+1, i)))

def isPrime(a):
    if a < 2:
        return False
    return a not in notPrimes


for i in range(int(input())):
    print('YES' if isPrime(int(input())) else 'NO')