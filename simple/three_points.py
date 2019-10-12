p = sorted([list(map(int, input().split())) for x in range(0, 3)], key=lambda p: p[0])
print(0 == ((p[1][0] - p[0][0]) * (p[2][1] - p[0][1]) - (p[1][1] - p[0][1]) * (p[2][0] - p[0][0])))

