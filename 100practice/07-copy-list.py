# http://www.runoob.com/python/python-exercise-example7.html

list1 = [1,2,3]
# In this way list2 is like a pointer to list1. What do to list1 will effect list2;
list2 = list1;
list1.append(4)

print (list1)
print (list2)

print ('-----------')

# list1 will be copied to list3 in this way;
list3 = list1[:]
list1.append(5)

print (list1)
print (list3)

print ('-----------')

# list1 will be copied to list3 in this way;
# use copy.copy(list1) in Python2
list4 = list1.copy()
list1.append(5)

print (list1)
print (list4)


