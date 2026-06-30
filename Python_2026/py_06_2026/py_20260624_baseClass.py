class car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(self.brand, " is driving at ", self.speed)

car1 = car("Tesla", 120)
car1.drive()