import requests
import urrlib3
url = "https://catfact.ninja/fact"
#response = requests.get("https://catfact.ninja/fact")
http = urllib3.PoolManager()
r = http.request("GET", url)
print(r.data)
print(r.status)
#print(response.json()["fact"])
