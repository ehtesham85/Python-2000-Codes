class Person:
   def __init__(self, name, age):
     self.name=name
     self.age=age
     self.version=1

p=Person("Ali", 30)
print(p.__dict__)
