# http://www.runoob.com/python/python-exercise-example20.html

#[100 50 50 25 25]

hight = [100]

time = int(input('time:'))
s = hight[0]

for i in range(1, time):
    hight.append(hight[i-1] / 2)
    print (i+1, ',', hight[i])
    s += hight[i] * 2

print (s)
