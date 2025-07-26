class Employee:
  def __init__(self):
    self.__name="Ehtesham"

a=Employee()
print(a.__name)          # can't accessed directly
print(a._Employee__name) # can be accessed indirectly


