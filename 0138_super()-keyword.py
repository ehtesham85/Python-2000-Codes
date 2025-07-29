class Parent:
   def parent_method(self):
     print("This is parent method")

class Child(Parent):
  
   def parent_method(self):
     print("Ehtesham")
     super().parent_method()
     
   def child_method(self):
      print("This is child method")
      super().parent_method()


child_object=Child()
child_object.child_method()

