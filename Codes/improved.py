import requests 
from bs4 import BeautifulSoup
import itertools
import webbrowser
import urllib 

fx = open('abbre.txt', 'r+')
fx.truncate()

file = open("name.txt", 'rU')
x = ":" ; WORD = "";

f= open("abbre.txt","w+")

for line in file:
	for word in line.split():
		qry = urllib.parse.quote_plus(word)
		#url = "http://www.abbreviations.com/serp.php?st="+qry+"&category=SMS&qtype=1"
		url2 = "http://www.abbreviations.com/serp.php?st="+qry+"&category=CHAT&qtype=1"
		#html = requests.get(url)
		html2 = requests.get(url2)
		#soup = BeautifulSoup(html.content,'html.parser')
		soup2 = BeautifulSoup(html2.content,'html.parser')
		print("="*45)
		print(word)
		#ab_data = soup.find_all("td",{"class":"tal dx"})
		AB_data = soup2.find_all("td",{"class":"tal dx"})
		for item2 in (AB_data):
			#abb_data = item.find_all("p",{"class": "desc"})
			ABB_data = item2.find_all("p",{"class": "desc"})
			for b in (ABB_data):
				WORD = WORD + str(x)+ str(b.text)
		f.write("*"+str(word)+str(WORD)+"#\n")
		WORD = ""
f.close()
