n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
numberOfInversions = 0
for i in range(n):
    for j in range(i, n):
        if array[i] > array[j]:
            numberOfInversions += 1
print(numberOfInversions)