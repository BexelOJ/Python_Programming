# Defining a class
class Dog:
    # Constructor method
    def __init__(self, name, breed):
        self.name = name      # attribute
        self.breed = breed    # attribute

    # Method
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects (instances)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "Labrador")

# Accessing attributes and methods
print(dog1.name)     # Output: Buddy
print(dog2.breed)    # Output: Labrador
dog1.bark()          # Output: Buddy says Woof!



