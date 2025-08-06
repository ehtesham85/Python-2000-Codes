# Calculate volume and surface area 
# V = 4/3*pi*r**3
# A = 4*pi*r**2

import math 

# Simple way to calculate the volume and surface area of a sphere
r = float(input("Enter the radius : "))
V = 4/3*3.14*r**3
A = 4*3.14*r**2
print("Volume : ", V)
print("Surface Area : ", A)


# Using math library to calculate the volume and surface area of a sphere
r = float(input("Enter the radius : "))
V = 4/3*math.pi*r**3
A = 4*math.pi*r**2
print("Volume : ", V)
print("Surface Area : ", A)