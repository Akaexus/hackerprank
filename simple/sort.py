input()
numbers = [int(x) for x in input().split()]
sortedNumbers = sorted(numbers)
print(' '.join(map(str, sortedNumbers)))
