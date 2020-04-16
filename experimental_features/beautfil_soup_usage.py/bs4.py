# -*- coding: utf-8 -*-

"""
    Library for extracting data from XML or HTML files
"""
from bs4 import BeautifulSoup
import urllib3 as urllib

url = "https://www.pythonforbeginners.com"
http = urllib.PoolManager()
response = http.request('GET', url)
content = response.data

soup = BeautifulSoup(content)

print(soup.prettify())

# print(title)
# >> 'title'? Python For Beginners

print(soup.title.string)
# >> ? Python For Beginners

print(soup.p)

print(soup.a)
#print(soup.get_text()) /Get all text
#txt=soup.get_text()

# Using the find_all method, gives us a whole list of elements with the tag "a". 
# link_listk
for link in soup.find_all('a'):
    print(link.get('href'))