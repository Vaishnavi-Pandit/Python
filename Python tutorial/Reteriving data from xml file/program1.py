#to retrive the data from a xml file
import xml.etree.ElementTree as ET
tree=ET.parse('E:\Python\datasets-df-series\cust-data.xml')#pasrsing means going through each node of tree.
root=tree.getroot()
print('root tag name: ',root.tag)
for child in root:
    print('child tag= ',child.tag)#.tag means tag name.
for c in root.findall('customer'):#customer is a child tag name
    a=c.attrib#attrib means attribute information only.
    print(a)
    print(a.get("type"))#get is used in dictionary to reterive values

    others1=c.find('place').text
    print('place= ',others1)

    others2=c.find('amount').text
    print('Amount= ',others2)