class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def show(self):
    print(f"The name of Employee {self.id} is {self.name} ")

class Programmer(Employee):
   def language(self):
      print("The default language is Python")


e1=Employee("Ehtesham",390)
e1.show()
e2=Programmer("Ali",90)
e2.show()
e2.language()

