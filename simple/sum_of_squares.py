a, b = list(map(int, input().split(' ')))
print(sum(list(map(lambda n: n*n, list(range(a, b+1))))))