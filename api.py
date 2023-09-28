import requests
import sys

res = requests.get(url=f"http://10.10.11.161/api/v1")
print(res)

data = res.json()
print(data)