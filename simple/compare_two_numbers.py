for i in range(0, int(input())):
    a, b = list(map(int, input().split(' ')))
    if a != b:
        print('{}  {}  {}'.format(a, 'is smaller than' if a < b else 'is greater than', b))
    else:
        print('n is equal m:  {}'.format(a))