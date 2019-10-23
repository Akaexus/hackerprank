size = int(input())
bitlength = (size-1) * 2
board = []
for i in range(size):
    board.append([int(x) for x in input().split()])
