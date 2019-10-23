# n = int(input())
# squares = [int(x) for x in input().split()][0:n:]
#
# maxMoves = []
# for i in range(0, n):
#     moves = 0
#     for x in range(i, n):
#         if squares[x-1]>=squares[x]:
#             moves += 1
#         else:
#             break
#     maxMoves.append(moves-1)
# if len(maxMoves):
#     print(max(maxMoves))
# else:
#     print(0)
n = int(input())
squares = [int(x) for x in input().split()][0:n:]
maxMoves = []
moves = 0
first = True
for i in range(1, n):
    if squares[i-1] >= squares[i]:
        moves += 1
    else:
        maxMoves.append(moves)
        moves = 0
maxMoves.append(moves)
print(max(maxMoves))
