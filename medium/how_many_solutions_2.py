import math

n, x, y = [int(x) for x in input().split()]

xdivy = x/y
solutions = 0
for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            dsquare = xdivy*(a*a-c*c)+b*b
            if dsquare >= 0:
                d = math.sqrt(dsquare)
                if 0 <= d <= n and d.is_integer():
                    solutions += 1
print(solutions)