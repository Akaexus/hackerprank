s = input()
print(sum(filter(lambda x: x>0 and x%2 == 0, map(int, s.split()))))