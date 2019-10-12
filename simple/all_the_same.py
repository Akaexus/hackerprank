n = int(input())

flag = True
first = 0
for i in range(0, n):
    if i == 0:
        first = int(input())
    else:
        if int(input()) != first:
            flag = False
print(flag)