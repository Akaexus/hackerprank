colSides = ['W', 'A', 'A', 'M', 'W']

for test in range(int(input())):
    seat = int(input())
    if seat == 1:
        print('poor conductor')
    else:
        row = (seat - 2) // 5 + 1
        column = (seat - 2) % 5
        if row % 2 == 1:
            side = 'L' if column <= 1 else 'R'
            colSide = colSides[column]
        else:
            side = 'R' if column <=2 else 'L'
            colSide = colSides[-column-1]
        print(row, colSide, side)
