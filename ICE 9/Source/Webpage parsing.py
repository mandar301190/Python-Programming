import requests
from bs4 import BeautifulSoup
import os

url= "https://en.wikipedia.org/wiki/News"
soure_code = requests.get(url)
plain_text = soure_code.text
soup = BeautifulSoup(plain_text, "html.parser")
result_list = soup.findAll('div')
b = soup.find('div',{'class': 'mw-parser-output'})
print(b.text)
for div in result_list:
    link = div.find('h1')
    print(link)


