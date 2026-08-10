#!/usr/bin/python3

class Test:
    count = 10  # static variable

    @staticmethod  # static method
    def add(a, b):
        return a + b

t = Test()

print(Test.count)
print(t.count)

print(Test.add(55, 65))
print(t.add(15, 25))



