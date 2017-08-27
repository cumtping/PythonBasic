# http://www.runoob.com/python/python-exercise-example18.html
from functools import reduce

n = int(input('n='))
x = int(input('x='))

s = 0
items = [x]

for i in range(n):
    print ('i=', i)
    s += items[i]
    first_num = 1
    # this can be optimized
    for j in range(i+1):
        first_num *= 10
    items.append(items[i] + x * first_num)

print ('s=', s)

print ('-------------')

Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print (Tn)
# what is reduce?
#   for each item in list call the function;
# what is lambda?
#   lambda x,y : x+y minds def f(x,y) return x+y;
# by the call below, we sum up all item in Sn;
Sn = reduce(lambda x,y : x + y,Sn)
print ("s=",Sn)