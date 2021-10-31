import requests
url = "https://catfact.ninja/fact"
response = requests.get("https://catfact.ninja/fact")
print(response.json())
print(response.json()["fact"])
