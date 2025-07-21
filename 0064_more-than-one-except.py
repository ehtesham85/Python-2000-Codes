try:
   num=int(input("Enter a number : "))
   a=[4, 5]
   print(a[num])
except ValueError:
   print("Entered number is not integer")
except IndexError:
   print("Index Error")
  
