#!/usr/bin/python3

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")


d = Dog("Tommy")

d.eat()
d.bark()


