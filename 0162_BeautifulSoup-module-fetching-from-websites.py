# Beautiful Soup Module
import requests
from bs4 import BeautifulSoup

url="http://www.codewithharry.com/blogpost/django-cheatsheet/"
r=requests.get(url)

soup=BeautifulSoup(r.text,"html.parser")
for heading in soup.find_all("h2"):
    print(heading.text)
  