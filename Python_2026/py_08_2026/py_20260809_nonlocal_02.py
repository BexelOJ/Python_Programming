#!/usr/bin/python3

x = 100                  # Global

def outer():
    x = 50               # Enclosing/local to outer

    def inner():
        #print(x)
        nonlocal x       # Uses outer's x
        x = 25
        print(x)

    inner()
    print(x)

outer()
print(x)


