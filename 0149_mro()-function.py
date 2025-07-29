class Employee:
  def __init__(self, name):
     self.name=name
  def show(self):
     print("The name is", self.name)


class Dancer:
   def __init__(self, dance):
      self.dance=dance

   def show(self):
      print("The dance is", self.dance)

class DancerEmployee( Dancer, Employee):
   def __init__(self, dance, name):
     self.dance=dance
     self.name=name

o=DancerEmployee("Break-Dance", "Micheal Jackson")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())
