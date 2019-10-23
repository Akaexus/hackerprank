n = int(input())

inverseResistors = [1/int(x) for x in input().split()]
print(1/sum(inverseResistors))

