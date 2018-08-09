import requests
import webbrowser


payload = dict(p="Shreyas Agarwal")
r = requests.post("file:///C:/Users/dell/Desktop/Page1.html", data=payload)
print(r.text)
URL = "file:///C:/Users/dell/Desktop/Page1.html"
webbrowser.open(URL)