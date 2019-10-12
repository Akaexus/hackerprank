from functools import reduce
lengths = reduce(lambda a, b: a*b, map(int, input().split(' ')))
print(lengths)