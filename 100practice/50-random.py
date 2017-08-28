import random

# float
print (random.uniform(10, 20))
# 0-1 float
print (random.random())
# int
print (random.randint(10, 20))
# by step
print (random.randrange(0, 101, 2))
# sample
print (random.sample('abcdefghij',3))
# choice
print (random.choice(['apple', 'pear', 'peach', 'orange', 'lemon']))

items = [1, 2, 3, 4, 5, 6]
random.shuffle(items)
print (items)
