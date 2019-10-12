edgeX = int(input())
rectanglesHeights = []
for i in range(0, edgeX):
    rectanglesHeights.append(int(input()))
# y |
#   |
#   |
#   |
#   |
#   |____________________ x
areas = []
for minX in range(0, edgeX):
    for maxX in range(minX, edgeX):
        if minX == maxX:
            height = rectanglesHeights[minX]
        else:
            height = min(rectanglesHeights[minX:maxX+1])
        areas.append(height * (maxX - minX + 1))
print(max(areas))