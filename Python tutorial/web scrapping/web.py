import urllib.request
import re

f = urllib.request.urlopen(r'file:///E:/Python/Python%20tutorial/Ragular%20expression/table.html')

data = f.read()
data1 = data.decode()
print(data1)

lst = re.findall(r'<tr><td>\w+</td><td>(\w+)</td><td>(\w+)</td><tr>', data1)

print(lst)
