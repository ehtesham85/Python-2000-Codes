# Decorators

def greet(fx):
  def mfx():
    print("Good Morning")
    fx()
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello World")

@greet
def add(a,b):
  return a+b

hello()
# add(5,10)   # this will not work because greet function does not take any arguments
