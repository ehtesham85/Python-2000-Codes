import requests

query=input("What type of news you are interested in? ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-09-09&sortBy=publishedAt&apiKey=5b753371231b435"
r=requests.get(url)
print(r.text)
news = json.loads(r.text)
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("------------------------------------")
  
