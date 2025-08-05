#  Multiprocessing

import multiprocessing
import requests

def FileDownload(url, name):
  response=requests.get(url)
  open(f"{name}.jpg","wb").write(response.content)

url="https://picsum.photos/200/300"
for i in range(5):
  FileDownload(url, i)
  print(f"Downloaded {i}")


