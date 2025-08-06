# Compute real roots of a quadratic equation
# use Math library

import math

print("This Program finds the real roots of a quadratic\n")
a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))

discroot=math.sqrt(b*b-4*a*c)
root1=(-b+discroot)/(2*a)
root2=(-b-discroot)/(2*a)

print("\nThe solutions are:",root1,root2)

