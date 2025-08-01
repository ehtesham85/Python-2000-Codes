# Generators 

def my_Generator():
   for i in range(100):
     yield i

gen = my_Generator()
# for n in gen:
  # print(n)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
