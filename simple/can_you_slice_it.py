indexes = sorted(list(map(int, input().split(' '))))

def canSlice(indices):
    startingDiff = 0
    for i in range(0, len(indices)-1):
        if i == 0:
            startingDiff = indices[1] - indices[0]
        else:
            if (indices[i+1] - indices[i]) != startingDiff:
                return False
    return True

print(canSlice(indexes))
