#! /usr/env/python3 

import requests
from bs4 import BeautifulSoup as bs

r = requests.get('http://pythonhow.com/example.html')
c = r.content

soup = bs(c, 'html.parser')
#print(soup.prettify()) -> show human nice readable sourcecode
divs = soup.find_all('div',{'class':'cities'})
h2s = []
ps = []

for item in divs:
    h2s.append(item.find_all('h2')[0].text)
    ps.append(item.find_all('p')[0].text)
    
print(h2s)
print(ps)