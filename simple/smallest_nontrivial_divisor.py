n = int(input())

def snd(number):
    for x in range(2, number+1):
        if number % x == 0:
            return x
    return False
print(snd(n))