# http://www.runoob.com/python/python-exercise-example12.html
import math

def is_prime(n):
  s = int(math.sqrt(n))
  for i in range(2, s+1):
    if n % i == 0:
      return False
  return True

for i in range(101, 201):
  if is_prime(i):
    print (i)
	