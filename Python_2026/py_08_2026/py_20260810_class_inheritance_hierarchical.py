#!/usr/bin/python3

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")

dog = Dog()
cat = Cat()

dog.eat()     # inherited from Animal
dog.bark()    # Dog's own method

cat.eat()     # inherited from Animal
cat.meow()    # Cat's own method

