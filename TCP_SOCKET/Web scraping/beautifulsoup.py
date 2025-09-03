#extracting informations from a web page
#py -m pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=py+-+m+pip+install"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

#Retrieve all of the anchor tags
# tags = soup('a')
tags = soup.find_all('h3')
for tag in tags:
    # print(tag.find('div').text)
    print(tag.get_text())

