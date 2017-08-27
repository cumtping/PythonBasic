# http://www.runoob.com/python/python-exercise-example8.html

for i in range(1, 10):
  one_line = []
  for j in range(1, i+1):
    one_line.append(str(j) + '*' + str(i))
  print (one_line)

for i in range(1, 10):
  print ('')
  for j in range(1, i+1):
    # In Python3, we use end='' to change default end \n to '', so that we don't return the line.
	# In Python2, we append , in the end of print to do this.
	# use %d to format string.
    print ("%d*%d=%d "%(i, j, i*j), end='')