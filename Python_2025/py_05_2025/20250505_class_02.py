class Cat:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
        
    def meow(self):
        print(f"{self.name} says Meow!")
        
        
c1 = Cat("puzzy", "cat_breed_01")
c2 = Cat("pingu","cat_breed_02")
print(f"Cat Name = {c1.name} ")
print(f"{c2.name}")
print(f"{c1.breed}")
print(f"{c2.breed}")
c1.meow()
c2.meow()






