import urllib.request

f=urllib.request.urlopen(r'location')

data=f.read()
data=data.decode()
print(data)
import re
lst= re.finadall()
