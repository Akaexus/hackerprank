import math
import cmath
inp = input().split('+')
a = int(inp[0])
b = int(inp[1][:-1])
z = complex(a, b)
d = (cmath.polar(z))

print(d[0])
print(round(d[1], 4))
