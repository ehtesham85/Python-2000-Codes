# Program calculate cost per square inch of a circular pizza, given its diameter and price.
import math

diameter = float(input("Enter diameter of pizza in inches : "))
price = float(input("Enter price of pizza in dollars : "))

r = diameter/2
A = math.pi * (r**2)

cost_per_inch = price/A

print(f"Area of pizza is {A:.2f}")
print(f"Cost per square inch is {cost_per_inch:.2f} dollars")
      
