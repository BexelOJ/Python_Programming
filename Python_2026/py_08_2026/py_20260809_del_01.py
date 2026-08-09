#!/usr/bin/python3

#####################################
# Delete a variable/reference:
x = 10

del x

print(x)   # ❌ NameError

#####################################
# Delete an object attribute:
class Person:
    pass

p = Person()
p.name = "Lr"

del p.name

print(p.name)    # ❌ AttributeError

#####################################
# Delete an element from a list:
numbers = [10, 20, 30]

print(numbers)

del numbers[1]

print(numbers)

#####################################
# With objects:
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Lr")

del p

#####################################


#####################################


#####################################


