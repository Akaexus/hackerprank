numbers = input().split()

def d(numbers):
    if len(numbers) == 1:
        return int(numbers[0])
    else:
        n = numbers.pop()
        return int(n)+d(numbers)

print(d(numbers))