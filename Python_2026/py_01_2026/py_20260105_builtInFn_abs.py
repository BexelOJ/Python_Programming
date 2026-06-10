import os

a = -15
b = 3.14
c = -100.98

abs_a = abs(a)
abs_b = abs(b)
abs_c = abs(c)

def display():
    print(f" a = {a}")
    print(f" b = {b}")
    print(f" c = {c}\n")

def display_absolute():
    print(f" Abs of a is {abs_a}")
    print(f" Abs of b is {abs_b}")
    print(f" Abs of c is {abs_c}\n")

if __name__ == "__main__":
    display()
    display_absolute()
    


