import time

def usingWhile():
    i=0
    while i<5000:
      i=i+1
      print(i)

def usingFor():
  for i in range(5000):
      print(i)


init=time.time()
usingFor()
print(time.time()-init)
usingWhile()
print(time.time()-init)
