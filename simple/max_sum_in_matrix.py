import sys

n = int(input())
matrix = []

sums = []

for line in sys.stdin:
    matrix.append(list(map(int, line.split())))

for x1 in range(0, n):
    for x2 in range(x1, n):
        for y1 in range(0, n):
            for y2 in range(y1, n):
                rows = matrix[y1:y2+1]
                s = 0
                for row in rows:
                    s += sum(row[x1:x2+1])
                sums.append(s)
print(max(sums))
