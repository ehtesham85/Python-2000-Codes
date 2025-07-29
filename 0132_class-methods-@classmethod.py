class Employee:
  company="Samsung"
  noOfEmployees=0
  def show(self):
    print(f"The name of the Employee is {self.name} and the company name       is {self.company}")

  @classmethod
  def changecompany(cls, newCompany):
      cls.company=newCompany

e1=Employee()
e1.name="Ehtesham"
e1.show()
e1.changecompany("Apple")
e1.show()
print(Employee.company)

