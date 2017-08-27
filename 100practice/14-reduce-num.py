#!/usr/bin/python
# -*- coding: UTF-8 -*-

def reduceNum(n):
    # string format, use {} insted of %, added from python 2.7, 
    # In [3]: '{1},{0},{1}'.format('kzc',18)  Out[3]: '18,kzc,18'
    # In [5]: '{name},{age}'.format(age=18,name='kzc')  Out[5]: 'kzc,18'
    print ('{} = '.format(n), end='')
    # isinstance 
    if not isinstance(n, int) or n <= 0 :
        print ('Please input a correct number')
        exit(0)
    elif n in [1] :
        print ('{}'.format(n))
    while n not in [1] : # 循环保证递归
        for index in range(2, int(n) + 1) :
            if n % index == 0:
                n /= index # n 等于 n/index
                if n == 1: 
                    print (index)
                else : # index 一定是素数
                    print ('{} *'.format(index), end='')
                break
reduceNum(90)
reduceNum(100)
