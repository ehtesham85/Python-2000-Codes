import time
import asyncio
import requests

async def function1():
    print("Function 1")
    URL="https://plus.unsplash.com/premium_photo-1686729237226-0f2edb1e8970?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8d2FsbHBhcGVyfGVufDB8fDB8fHww"
    response=requests.get(URL)
    open("instagram.ico","wb").write(response.content)


async def function2():
  print("Function 2")
  URL="https://images.pexels.com/photos/268533/pexels-photo-268533.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
  response=requests.get(URL)
  open("facebook.ico","wb").write(response.content)


async def function3():
  print("Function 3")
  URL="https://images.pexels.com/photos/1421903/pexels-photo-1421903.jpeg?cs=srgb&dl=pexels-eberhardgross-1421903.jpg&fm=jpg"
  response=requests.get(URL)
  open("whatsapp.ico","wb").write(response.content)


async def main():
   # #first method
   # await function1()
   # await function2()
   # await function3()

   L= await asyncio.gather(function1(),function2(),function3())
   print(L)


asyncio.run(main())
