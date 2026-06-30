class Base_one:
   def origin(self):
      print("Hello from One, I'm comming")

   def priting_one(self):
      print("Hello World from one")

class Base_two(Base_one):
   def origin(self):
      print("Hello fron two, I'm comming")

   def priting_two(self):
      print("Hello World from two")

class Derived(Base_two):
   def india(self):
      print("Hello from India")


if __name__ == "__main__":
   derObj = Derived()
   derObj.origin()
   derObj.origin()  
   derObj.india()
   derObj.priting_one()
   derObj.priting_two()


