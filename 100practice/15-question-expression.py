# http://www.runoob.com/python/python-exercise-example15.html

score = int(input('score:'))

# seems no (a>b)?a:b in python
print (if score >= 90  'A' else (if score >= 60 'B' else 'C'))