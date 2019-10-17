john, betty = [int(x) for x in input().split()]
print('John' if john > betty else ('Betty' if betty > john else 'NOBODY'))
