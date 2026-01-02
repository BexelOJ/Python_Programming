class Adder:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    
    def addition(self, a=0, b=0):
        if a == 0 and b == 0:
            return self.a + self.b
        return a + b

class Subtractor:
    def __init__(self, c=0, d=0):
        self.c = c
        self.d = d;

    def subtraction(self, c=0, d=0):
        return c - d

obj1 = Adder()

obj2 = Subtractor()

print()
print(obj1.addition(0,4))
print(obj1.addition(215))
print(obj1.addition())
print()
print(obj2.subtraction(8,3))
print(obj2.subtraction(5))
print(obj2.subtraction())

