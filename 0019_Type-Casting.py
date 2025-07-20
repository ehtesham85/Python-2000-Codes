a=1
a="1"
b=2
b="2"
print(a+b)           # Concatenation (add sting to strings side by side)
print(int(a)+int(b)) # Type-Casting Convert String to Integer

# Implicit Type-Casting
c=1.9
d=8
print(c+d)

# Python automatically converts x to int
x=7
print(x)
print(type(x))

# Python automatically converts y to float
y=3.0
print(y)
print(type(y))

# Python automatically converts z to float as it is a float addition
z=x+y
print(z)
print(type(z))