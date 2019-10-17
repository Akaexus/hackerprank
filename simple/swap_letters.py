input()
numbers = [int(x) for x in input().split()]

while 1:
    try:
            inp = input()
            x, y = [int(x) for x in inp.split()]
            numbers[x], numbers[y] = numbers[y], numbers[x]
    except:
        break
print(' '.join(map(str,numbers)))
