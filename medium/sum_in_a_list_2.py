l = [int(x) for x in input().split()]
for input_index in range(int(input())):
    i, j = [int(x) for x in input().split()]
    lsum = 0
    for index in range(i, j+1):
        lsum += l[index]
    print(lsum)