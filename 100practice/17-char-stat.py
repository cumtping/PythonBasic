#http://www.runoob.com/python/python-exercise-example17.html
import operator

str = input('input string:')

len = len(str)
alpha = 0
blank = 0
num = 0
other = 0

def is_num_by_exception(n):
    try:
        int(n)
        return True
    # what is ValueError? funtction arguments error
    # other errors:
    #    NameError, call not declared variables
    #    ZeroDivisionError
    #    SyntaxError
    #    IndexError
    #    KeyError
    #    IOError
    #    AttributeError
    except ValueError:
        return False

for i in range(len):
    if str[i].isalpha():
        print (str[i], ' is alpha')
        alpha+=1
    elif str[i].isdigit():
        print (str[i], ' is digit')
        num+=1
    # cmp is defined in python2, but is decrepated in python3
    # import operator instead.
    elif operator.eq(str[i], ' '):
        print (str[i], ' is blank')
        blank+=1
    else:
        print (str[i], ' is other')
        other+=1

print ('alpha=%d blank=%d num=%d other=%d'%(alpha, blank, num, other))

    