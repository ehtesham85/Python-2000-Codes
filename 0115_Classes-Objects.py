class Person:
  name="Ehtesham"
  age=21
  occupation="Software Developer"
  def info(self):
    print(f"{self.name} is a {self.occupation}")

a=Person()
a.info()

#Update information in class variables
# a.name="Ali"
# a.age=20
# a.occupation="Student"
# a.info()