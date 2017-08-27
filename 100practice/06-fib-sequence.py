# http://www.runoob.com/python/python-exercise-example6.html
# fab[0]=0, fab[1]=1, fab[2]=1;

def fab(n):
  # Waoooo! we can define like this!
  a,b=0,1
  for i in range(n):
    a,b=b,a+b
  return a
  
for i in range(10):
  print ('fab[', i, ']=', fab(i))
  
print ('--------------')
l = [0,1]

def fab2(n):
  # range does not inclue n+1 here.
  for i in range(2, n+1):
    l[i] = l[i-1] + l[i-2]
    
  return l[n]

for i in range(10):
  print ('fab2[', i, ']=', fab(i))
  
print ('--------------')

def fab3(n):
  if n==0:
    return 0;
  if n==1:
    return 1;
  return fab3(n-1) + fab3(n-2)

for i in range(10):
  print ('fab3[', i, ']=', fab(i))
  
# which one is more efficient?
#