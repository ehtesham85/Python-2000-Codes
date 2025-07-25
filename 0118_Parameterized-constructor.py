class Person:
  def __init__(self, n, o):
     print("Hey I am a person")
     self.name=n
     self.occupation=o
  
  def info(self):
    print(f"{self.name} is a {self.occupation}")

a=Person("Ehtesham","Programmer")
b=Person("Ali","Student")
a.info()
b.info()
