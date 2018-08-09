import requests #helps extracting the web page. 
from bs4 import BeautifulSoup #helps scrapping data from the website.
import urllib # converts the given string into url specific format.

# opens the file and delete's every content in the file.
fx = open('abbre.txt', 'r+')
fx.truncate()

#opens the file that contains the abbrevations.

file = open("name.txt", 'rU')
x = " : " ; WORD = "";

# opens the file in which new abbrevation + full form is being given.

f= open("abbre.txt","w+")

for line in file: #searches every line in the file
	for word in line.split(): #splits the words in each line that is being acquired by the above for loop.
		qry = urllib.parse.quote_plus(word) #converts the qry into url format.
		url = "http://www.abbreviations.com/serp.php?st="+qry+"&category=CHAT&qtype=1" #generates the actual website webpage.
		html = requests.get(url) #get's the url of the website.

		soup = BeautifulSoup(html.content,'html.parser') 
		print("="*45)
		print(word)
		ab_data = soup.find_all("td",{"class":"tal dx"}) #get's the data from the tag specified
		for item in ab_data:
			abb_data = item.find_all("p",{"class": "desc"}) #get's the context of the tag from where the actual data is to be extracted.
			for a in abb_data:
				WORD = WORD + str(x)+str(a.text) #generates the string value which is to be written in the file
		f.write("*"+str(word)+str(WORD)+"#\n") #writes the value of the string in the specific format for easier retrieval of the expansion of the word specified.
		WORD = "" #reassign the value so that new values can be added.
f.close() #closes the file in order & saves the newly created documents.
