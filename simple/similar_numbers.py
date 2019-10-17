input()
numbers = [int(x) for x in input().split()]

def checkSimilar(numbers):
    for a in numbers:
        for b in numbers:
            if abs(a-b) == 1:
                return 'YES'
    return 'NO'

print(checkSimilar(numbers))