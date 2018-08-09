txt = '''hello, my name is Shreyas Agarwal. Diwali is a festival with lots of lights. by the weight of the crackers 
		it's hardly impossible to burst them in a single night. So take care guys. Wish u a Happy Diwali.'''

import re


def gen(s):
    return ' '.join([i+'+\w+' for i in s])

file = open("name.txt", 'rU')


import requests 
from bs4 import BeautifulSoup 
import urllib 


fx = open('abbre.txt', 'r+')
fx.truncate()


file = open("name.txt", 'rU')
y = " : " ; WORD = "";
m = [];k = []
X = " ";Let = " ";new = " "


f= open("abbre.txt","w+")

def checker(WORD,X):
	for i in WORD.split(":"):
		m.append(i.strip())
	for j in range(0,len(X)):
		for i in range(0,len(m)):
			if(m[i] == 	X[j]):
				k.append(X[j])
	new = ''.join(list(set(X)-set(k)))
	return new

for line in file: 
	for word in line.split(): 
		x = re.findall(gen(word.lower()),txt)
		if (x != [] ):
			Let = word ;
			X = x;

		qry = urllib.parse.quote_plus(word) 
		url = "http://www.abbreviations.com/serp.php?st="+qry+"&category=CHAT&qtype=1" 
		html = requests.get(url) 

		soup = BeautifulSoup(html.content,'html.parser') 
		ab_data = soup.find_all("td",{"class":"tal dx"}) 
		for item in ab_data:
			abb_data = item.find_all("p",{"class": "desc"}) 
			for a in abb_data:
				WORD = WORD + str(y)+str((a.text).lower())
		new = checker(WORD,X)
		if ( new.strip() != ""):
			print(new)
			print(str(word)+" is "+'Updated.')
			WORD = WORD + str(y) + str(new.strip())
		f.write("*"+str(word)+str(WORD)+"#\n") 
		m = []
		k = []
		X = " "
		Let = " "
		new = " "
		WORD = " "
f.close()