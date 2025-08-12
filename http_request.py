import requests


#Python get method
# r = requests.get("https://online.uom.lk/")
# print(r.url)
# print(r.status_code)
# print(r.text)

#parameterized get request
# q = requests.get('https://www.google.com/search?q=python')
# print(q.url)
# print(q.status_code)
# print(q.text) #the html content of the page


#Python requests POST method
url = "https://httpbin.org/post"
params = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, data=params)
print(r.url)
print(r.status_code)
print(r.text)