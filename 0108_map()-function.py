# map function
def cube(x):
    return x*x*x

l=[1, 2, 4, 6, 4, 3]
newl=list(map(cube, l))
print(newl)