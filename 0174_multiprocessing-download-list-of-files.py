#  Multiprocessing

import multiprocessing
import requests

def FileDownload(url, name):
  print(f"Started Downloading {name}")
  response=requests.get(url)
  open(f"f/file{name}.jpg","wb").write(response.content)
  print(f"Finished Downloading {name}")

# method 1
# url="https://picsum.photos/200/300"
# for i in range(5):
#   FileDownload(url, i)
#   print(f"Downloaded {i}")


# method 2
url="https://picsum.photos/200/300"
pros=[]
for i in range(5):
   p=multiprocessing.Process(target=FileDownload, args=[url, i])
   p.start()
   pros.append(p)

for p in pros:
  p.join
  
