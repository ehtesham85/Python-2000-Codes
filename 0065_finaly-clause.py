try:
   l=[1,2,3,4,5]
   i=int(input("enter the number"))
   print(l[i])
except:
   print("some error occured")
finally:
   print("I'm always executed man")       # always executes even error occured

