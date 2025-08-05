
import requests

URL=str(input("Enter the URL for Image download : "))
print("Image is downloading........")
response=requests.get(URL)
open("image.ico","wb").write(response.content)
print("Image downloaded successfully")



