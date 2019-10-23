letters = [int(x, 2) for x in input().split()]
print(''.join(list(map(chr, letters))))