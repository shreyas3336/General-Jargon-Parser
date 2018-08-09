import re

text = "hey, wassup, i will be right back to you. Good morning, have a nice day lots of love. Good night.".lower()
def generate(s):
    k = ''
    for i in s:
        k = k + str(i) + str('+\w+ ')
    k = k.strip()
    return k
a = '''def gen(s):
    return ' '.join([i+'+\w+' for i in s])'''

file = open("name.txt", 'rU')

a = '''print(re.findall(generate('brb'),text))'''




for line in file: #searches every line in the file
	for word in line.split():
		x = re.findall(generate(word.lower()),text)
		if (x != [] ):
			print(word.lower())
			print(x)

