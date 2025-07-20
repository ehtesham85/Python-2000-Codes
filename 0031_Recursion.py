#                    Recursion


#Factorial of a number by Recursion
def factorial(n):
  if(n==0 or n==1):
     return 1
  else:
    return n*factorial(n-1)

print(factorial(5))
#5 * factorial(4)
#5 * 4 * factorial(3)
#5 * 4 * 3 * factorial(2)
#5 * 4 * 3 * 2 * factorial(1)
#5 * 4 * 3 * 2 * 1

#Fibonacci sequence by Recursion
def fibonacci(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  elif(n==2):
    return fibonacci(1)+fibonacci(0)
  elif(n>2):
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))



