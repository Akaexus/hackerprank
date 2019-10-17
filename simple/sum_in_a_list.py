integers = [int(x) for x in input().split()]
i, j = [int(x) for x in input().split()]

print(sum(integers[i:j+1:]))