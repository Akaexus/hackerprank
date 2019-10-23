s = input()
print(sum(map(lambda x: x*x, range(int(s.split()[0]), int(s.split()[1])+1))))