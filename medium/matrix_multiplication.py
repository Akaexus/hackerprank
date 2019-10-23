x1, y1 = [int(x) for x in input().split()]
a1 = []
for rowNumber in range(y1):
    a1.append([int(x) for x in input().split()])

x2, y2 = [int(x) for x in input().split()]
a2 = []
for rowNumber in range(y2):
    a2.append([int(x) for x in input().split()])

a3 = []

for row in a1:
    newRow = []
    for colNumber in range(0, x2):
        col = [a2Row[colNumber] for a2Row in a2]
        _sum = 0
        for i in range(0, len(row)):
            _sum += row[i] * col[i]
        newRow.append(_sum)
    a3.append(newRow)
print('\n'.join([' '.join(map(str, row)) for row in a3]))
