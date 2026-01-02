class Adder:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        if a != 0:
            print("Parameterized Construtor Called")
        else:
            print("Default Constructor Called")

    def add(self):
        return self.a + self.b

obj1 = Adder(5,4)
obj_2 = Adder()

res = obj1.add()
res_2 = obj_2.add()

print("Sum: ", res)
print("Sum: ", res_2)


