n, k = input().split()
n = int(n)
k = int(k)
firstPart = list(range(n, 1-k, -k))
secondPart = list(range(firstPart[-1], n+1, k))[1::]
l = firstPart + secondPart

def printSpaced(array):
    if len(array) == 1:
        return str(array[0])
    else:
        return str(array[0]) + ' ' + printSpaced(array[1::])

print(printSpaced(l))