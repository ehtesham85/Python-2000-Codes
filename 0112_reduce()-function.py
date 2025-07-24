from functools import reduce
numbers=[1,2,3,4,5]
def sum(x,y):
  return x+y
mysum=reduce(sum,numbers)
print(mysum)

