class Student:

  def __init__(self):
    self._name = "Ehtesham"

  def _funname(self):
    return "Hello"


class Subject(Student):
  pass


obj = Student()
obj1 = Subject()

# calling by object of Student Class
print(obj._name)
print(obj._funname())

# calling by object of Subject Class
print(obj1._name)
print(obj1._funname())
