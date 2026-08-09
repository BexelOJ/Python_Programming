#!/usr/bin/python3

z = 10
def func1():
    z = 5
    print(z)
    global z
    z = 3

def func2(x,y):
    global z
    return x+y+z


func1()
total = func2(4,5)
print(total)


