#!/usr/bin/python3

def f(x,y):
    #print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print(f'You called f(x,y) with the value x = {x} and y = {y}')
    # print("x * y = " + str(x*y))
    print(f"x * y = {x*y}")
    return x*y

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

mul=f(x,y)

print(mul)


#def function(parameters):
#    instructions
#    return value

