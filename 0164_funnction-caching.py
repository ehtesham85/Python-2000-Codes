# Function Caching

from functools import lru_cache
import time

# @lru_cache(maxsize=None)
# def fx(n):
#    time.sleep(5)
#    return n*5

# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")
# # here, its move fast because same function is not called again and again
# print(fx(20))
# print("done for 20")
# print(fx(2))
# print("done for 2")
# print(fx(6))
# print("done for 6")




@lru_cache(maxsize=None)
def fib(n):
   if n<3:
     return n
   return fib(n-1)+fib(n-2)

print(fib(20))
