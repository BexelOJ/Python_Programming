class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

d1 = Dog("Buddy", 12)

print(d1.name)
print(d1.age)

s = d1.bark()
print(s)

d2 = Dog("Coddy",3)

if d2.age >= 3:
    print(True)



