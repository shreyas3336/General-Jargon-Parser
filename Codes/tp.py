import requests 
from bs4 import BeautifulSoup
import itertools
import webbrowser
import urllib 

fx = open('abbre.txt', 'r+')
fx.truncate()

file = open("name.txt", 'rU')
x = ":" ; 

f= open("abbre.txt","w+")

qry = "";
cat = "";
def resource(qry,cat,word):
	WORD = "";
	url = "http://www.abbreviations.com/serp.php?st="+qry+"&category="+cat+"&qtype=1"
	html = requests.get(url)
	soup = BeautifulSoup(html.content,'html.parser')
	print(word)
	ab_data = soup.find_all("td",{"class":"tal dx"})
	AB_data = soup2.find_all("td",{"class":"tal dx"})
	for item,item2 in zip(ab_data,AB_data):
		abb_data = item.find_all("p",{"class": "desc"})
		ABB_data = item2.find_all("p",{"class": "desc"})
		for a,b in zip(abb_data,ABB_data):
			if (str((a.text).strip) == ""):
				resource(qry,str("INTERNET"),word)
			WORD = str(WORD) + str(x) + str(a.text)
	f.write("*"+str(word)+str(WORD)+"#\n")
	WORD="";

for line in file:
	for word in line.split():
		qry = urllib.parse.quote_plus(word)
		resource(qry,str("SMS"),word)
		
f.close()
