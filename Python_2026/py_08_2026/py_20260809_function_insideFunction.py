#!/usr/bin/python3

import math

def subtraction(a,b):
    sub=(a-b)
    return a - b

def addition(x,y):
    sum = x + y
    sub=subtraction(x,y)
    return sum, sub

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

x,y=addition(a,b)

print(f"{a} + {b} = {x}")
print(f"{a} - {b} = {y}")

