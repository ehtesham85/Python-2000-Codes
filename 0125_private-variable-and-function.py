class Student:

  def __init__(self, name, age):
    self.__age = age

  def __funName(self):
    self.y = 34
    print(self.y)


class Subject(Student):
  pass


obj = Student("Ehtesham", 22)
obj1 = Subject

# print(obj.__age)                # through error because __age is private
print(obj._Student__age)  # print 22
# print(obj.__funName())          # through error because __funName is private
print(obj._Student__funName())  # print 34
