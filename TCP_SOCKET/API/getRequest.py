import requests
base_url =  "http://host1.open.uom.lk:8080"

response = requests.get(f"{base_url}/api/products/")
data = response.json()
print(len(response.json()["data"]))
# print(data)
