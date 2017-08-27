# http://www.runoob.com/python/python-exercise-example5.html

l = []

for i in range(3):
  x = int(input('integer:'))
  l.append(x)

print ('raw list:', l)
  
# Use sorted to do this. What's the difference with sort?
# 1. sort is the function of list, so it can only be called with list, 
#    while sorted can be called by all iterative object.
# 2. sort do the process with the old data while sorted create a new data;
print ('after sorted:', sorted(l))
print ('after sorted reversely:', sorted(l, reverse=True))

# sort the list, default from small to big; return None;
# how to sort reversely?  
l.sort()
print ('after sort:', l)
l.sort(reverse=True)
print ('after sort reversely:', l)
