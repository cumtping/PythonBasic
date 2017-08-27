# http://www.runoob.com/python/python-exercise-example19.html
import math

# all factor? not reduce number!!!
# 6: 1 2 3
# 28: 1 2 14 4 7
def add_up_all_factor(n):
    sum = 0
    #sqrt = int(math.sqrt(n
    half = int(n / 2)
    for i in range(2, half+1):
#        print ('before:i=%d n=%d sum=%d'%(i, n, sum))
        if n % i == 0:
            sum += n / i
            sum += i
#            print ('after:i=%d n=%d sum=%d'%(i, n, sum))
    return sum / 2 + 1

#test = int(input('test='))
#add_up_factor(test)
for i in range(2, 1001):
    if i == add_up_all_factor(i):
        print (i)
        
print ('---------------')

from sys import stdout
for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)
    
    if s == 0:
        print (j)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print (k[n])
