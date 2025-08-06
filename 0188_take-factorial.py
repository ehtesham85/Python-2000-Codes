# Take factorial using list

fact = 1
for factor in [6, 5, 4, 3, 2, 1]:
   fact=fact*factor
print("The factorial of 6 is",fact)


n=int(input("ENter a whole number : "))
fact = 1
for factor in range(n, 1,-1):
  fact=fact*factor
print("The factorial of",n,"is",fact)
