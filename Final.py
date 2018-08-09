import re
text = str(input())
txt = (((((text).upper()).replace("."," . ")).replace("!"," ! ")).replace("?"," ? ")).replace(","," , ")

v=[]
flag=0;
full_form=""
def default(h,val):
	g = open('Files/'+str(h).lower()+'.txt','r+')
	for l in g:
		for w in l.split("!"):
			if(w.strip()!=""):
				v.append(w.strip())
	TXT[val]=v[-1].upper();

def gen(s):
    return ' '.join([i+'+\w+' for i in s])

file = ['Files/ambi.txt','Files/unambi.txt'];
abbre =[]
f=[];
x="";
y="";
val=-1; 
def find(txt):
	ambi = open('Files/ambi2.txt','r+')
	unambi = open('Files/unambi2.txt','r+')
	for line in ambi:
		for word in line.split():
			x = re.findall(gen(word.upper()),txt);
			if (x!=[]):
				f.append(0)
				abbre.append(word)
	for line2 in unambi:
		for word2 in line2.split():
			y = re.findall(gen(word2.upper()),txt);
			if (y!=[]):
				f.append(1)
				abbre.append(word2)
	ambi.close();
	unambi.close();
find(txt)
if (len(abbre)>0):
	print("Abbreivation whose Full Form Found in the sentence is/are : ",len(abbre))
	for i in range(0,len(abbre)):
		print(abbre[i])


fault ="";

r=[]
abbre1 =[];
abbre2 =[];
f=[];
x="";
y="";
flag = -1;
TXT = txt.split();

def search(value):
	ambi = open('Files/ambi2.txt','r+')
	unambi = open('Files/unambi2.txt','r+')
	for line in ambi:
		for word in line.split("*"):
			if (value == word.strip().upper()):
				abbre1.append(word.strip())
				f.append(0);
	for line2 in unambi:
		for word2 in line2.split("*"):
			if(value == word2.strip().upper()):
				abbre2.append(word2.strip())
				f.append(1);
	ambi.close();
	unambi.close();

for i in range(0,len(TXT)):
	search(str(TXT[i]))

print("Abbreivation found in the sentence are: ",len(abbre1)+len(abbre2))
print("Ambiguous: ",abbre1)
print("Unambiguous: ",abbre2)

check = []
loc = []

def finder(val):
	flag=0;
	for i in range(0,len(check)):
		if(check[i]==loc[0] and check[i+1]==loc[1]):
			#print(check[i],loc[0],check[i+1],check[i],i,len(check),len(check)-3)
			if(i<=(len(check)-3)):
				full_form = check[i+2]
				flag=1;
		else:
			default(fault,val)
	if(flag==1):
		TXT[val] = full_form

def locate(ABB):
	lt = -1; rt = -1;
	k =str('Files/')+str(ABB).lower()+'.txt';
	file = open(k,'r+');
	for line in file:
		for word in line.split("*"):
			if ((word.upper()).strip()!=""):
				check.append((word.upper()).strip());
	file.close();

	#to find the left and right member of the abbrevation in the sentence.
	for i in range(0,len(TXT)):
		if(TXT[i]==ABB):
			val=i;
			#print("location :",i);
			if(i==0):
				loc.append("#")
				loc.append(TXT[i+1])
			if (i==len(TXT)-1):
				loc.append(TXT[i-1]);
				loc.append("#")
			else:
				loc.append(TXT[i-1]);
				loc.append(TXT[i+1]);
	finder(val)

def locater(a):
	maps = open('Files/unambi.txt','r+')
	for l in maps:
		for w in l.split("*"):
			if ((w.upper()).strip()==a.upper()):
				for j in l.split("*"):
					if ((j.upper()).strip()!=""):
						r.append(j.upper());
	for i in range(0,len(TXT)):
		if(TXT[i]==a):
			TXT[i]=r[1]

for n in f:
	if(n==0):
		for i in range(0,len(abbre1)):
			loc=[];
			check=[];
			val=-1;
			fault=abbre1[i];
			locate(abbre1[i]);
	if(n==1):
		for i in abbre2:
			locater(i);
			r=[];


print("Old Sentence:",txt.strip())
print("New Sentence:",' '.join([i for i in TXT]))
