import math

x = int(input("Enter a number : "))
guess = int(input("Enter your guess : "))
value = (guess + x/guess) / 2
print("The value is : ", .value)
print("The square root is : ", math.sqrt(x))
if(value == math.sqrt(x)):
    print("Your guess is correct")
else:
    print("Your guess is incorrect")