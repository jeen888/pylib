import linecache
import random

for i in range(5):
    no = random.randint(1, 100)
    print(str(no) + ': ' + linecache.getline('saying.txt', no))
