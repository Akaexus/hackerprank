from random import random
size = 100
for i in range(size):
    print(' '.join([str(round(random()*100)) for j in range(size)]))
