# A regular expression to retrive the main string
import re
st="dfgg fggd rt5t 657686 hhth 5565 f565"
lst=re.findall(r'\D+',st)
print(lst)

# regex yo retrieve names starting with 'an' or'ak'
str='anil akhil anant arun arati arundhati abhijit ankur akheera ant'
lstt=re.findall(r'a[nk]\w+',str)
print(lstt)
# retrieve birth dates :
data='gdfgd 23-4-5676, dgfh 44-5-6567, rtyr 5-7-4435'
stp=re.findall(r'\d{1-2}\d-\d{1-2}\d-\d{1-4}\d',data)
print(stp)

t="Kumbhmela will be conducted at the amhedabad in india."
str1=re.sub(r'amhedabad',r'aurangabad',t)
print(str1)