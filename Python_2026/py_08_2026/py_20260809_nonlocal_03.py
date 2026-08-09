#!/usr/bin/python3

x = 100

def outer():
    x = 200
    def inner():
        global x
        x = 300

    inner()
    print("outer:", x)

inner_result = outer()
print("global:", x)


