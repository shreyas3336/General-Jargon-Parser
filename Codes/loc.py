import requests #helps extracting the web page. 
from bs4 import BeautifulSoup #helps scrapping data from the website.
import urllib

lists =[]
url = "https://geoiptool.com/"
html = requests.get(url)
soup = BeautifulSoup(html.content,'html.parser') 
ab_data = soup.find_all("div",{"class":"sidebar-data hidden-xs hidden-sm"})
for item in ab_data:
	abb_data = item.find_all("div",{"class": "data-item"})
	for a in abb_data:
		lists.append(a.text);
print(lists[3],lists[5])