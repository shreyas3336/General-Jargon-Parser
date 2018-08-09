import re

txt = "hey, wassup, i will be right back to you. Good morning, have a nice day lots of love. Good night.".lower()

def gen(s):
    return ' '.join([i+'+\w+' for i in s])

file = open("name.txt", 'rU')

for line in file: #searches every line in the file
	for word in line.split():
		x = re.findall(gen(word.lower()),txt)
		if (x != [] ):
			print(word.lower())
			print(x)