class Employee:
    def __init__(self, name, id):
       self.name=name;
       self.id=id

class Programmer(Employee):
    def __init__(self, name, id, lang):
      super().__init__(name, id)
      self.lang=lang

ALi=Employee("Ali Don","420")
Ehtesham=Programmer("Ehtesham","421","Python")
print(Ehtesham.name)
print(Ehtesham.id)
print(Ehtesham.lang)
