class Bat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def fly(self):
        print(f"{self.name} is flying!")
        
b1 = Bat("Batty", 45)
b2 = Bat("Catty",3)
b1.fly()
print(f"{b1.name} is {b1.age} years old.")  
b2.fly()
print(f"{b2.name} is {b2.age} years old.")
        