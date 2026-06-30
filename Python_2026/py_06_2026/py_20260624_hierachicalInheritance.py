class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()

c = Cat()
c.speak()


