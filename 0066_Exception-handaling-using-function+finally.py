def func1():
  try:
     l=[1,2,3,4,5]
     i=int(input("Enter the number :"))
     print(l[i])
     return 1
     
  except:
     print("some error occured")
     return 0
     
  finally:
     print("I'm always executed man")       # always executes even error occured


print(func1())
