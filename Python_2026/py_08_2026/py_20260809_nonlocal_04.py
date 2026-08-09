#!/usr/bin/python3

x = 100

def outer():
    x = 200
    def inner():
        nonlocal x
        x = 300

    inner()
    print("outer:", x)

inner_result = outer()
print("global:", x)



# local      → current function

# nonlocal   → nearest enclosing function

# global     → module/global scope

# L → Local
# E → Enclosing
# G → Global
# B → Built-in


