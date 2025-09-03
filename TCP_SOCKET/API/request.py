import requests

BASE_URL = "http://localhost:8000"

response = requests.get(f"{BASE_URL}/vehicles/CBBB")
print(response.status_code)
print(response)