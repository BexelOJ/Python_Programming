#!/usr/bin/python

def f(x,y):
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x*y))
    z = 4 # cannot reach z, so THIS WON'T WORK
    print(z)

z = 3
f(3,2)
print(z)


