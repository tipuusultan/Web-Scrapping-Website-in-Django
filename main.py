import requests
from bs4 import BeautifulSoup

url = input("f")
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content , 'html.parser')
print(soup)