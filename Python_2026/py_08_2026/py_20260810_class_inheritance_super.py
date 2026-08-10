#!/usr/bin/python3

class Animal:
    def __init__(self, name):
        self.name = name

  #  def display():
  #      print(self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Tommy", "Labrador")


# d.display()


