#!/usr/bin/python3

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")

        
d = Dog()

d.eat()    # inherited from Animal
d.bark()   # Dog's own method



# Inheritance learning sequence:

# 1. Basic inheritance
#        ↓
# 2. Parent/child classes
#        ↓
# 3. __init__()
#        ↓
# 4. super()
#        ↓
# 5. Method overriding
#        ↓
# 6. Polymorphism
#        ↓
# 7. isinstance()
#        ↓
# 8. issubclass()
#        ↓
# 9. Multiple inheritance
#        ↓
# 10. MRO (Method Resolution Order)
#        ↓
# 11. Diamond problem
#        ↓
# 12. Abstract base classes
#        ↓
# 13. Composition vs inheritance



