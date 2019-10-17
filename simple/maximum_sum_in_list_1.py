numbers = [int(x) for x in input().split()]

sums = []
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        sums.append(sum(numbers[i:j+1]))
maxSum = max(sums)
if maxSum < 0:
    print(0)
else:
    print(maxSum)