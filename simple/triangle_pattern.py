height = int(input())
n = int(input())
for segment in range(0, n):
    for i in range(1, height+1):
        print(' '.join(['*'] * i))
    height += 1