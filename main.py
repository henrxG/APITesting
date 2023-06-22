import requests

response=requests.get("https://randomfox.ca/floof/")
print(response.json())
fox=response.json()
print(fox["image"])