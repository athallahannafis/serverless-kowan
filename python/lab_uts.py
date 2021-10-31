import requests
import urrlib3
url = "https://catfact.ninja/fact"
response = requests.get("https://catfact.ninja/fact")
print(response.json()["fact"])
