# Decorators

def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello World")

# @greet
def add(a,b):
  print(a+b)

hello()
# add(5,10)   # this will not work because greet function does not take any arguments
greet(add)(1,2)
