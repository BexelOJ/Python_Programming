#!/usr/bin/python3

class Animal:
    def sound(self):
        print("Animal sound")
    
    def color(self):
        print("Animal color")

class Dog(Animal):
    def sound(self):
        print("Bark")

    def color(self):
        super().color()
        print("Brown Dog")

a = Animal()
d = Dog()

a.sound()
d.sound() # The Dog version overrides the Animal version

d.color()

