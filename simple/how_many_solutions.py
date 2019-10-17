n, x, y = [int(x) for x in input().split()]
numberOfSolutions = 0
for a in range(n + 1):
    for b in range(n + 1):
        for c in range(n + 1):
            for d in range(n + 1):
                if x*(a*a-c*c) == y*(d*d-b*b):
                    numberOfSolutions += 1
print(numberOfSolutions)