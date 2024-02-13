# split the string where 1 or more numeric characterers are found
import re
st = "cxfs gfh 6464 dfgd 56574 fgd 56546"
lst = re.split(r' \d+', st)
print(lst)

qt="Hello World!"
t=re.search(r'^He',qt)
if t:
    print('found')
else:
    print('not found')
m=re.search(r'ld!$',qt)
if m:
    print('found')
else:
    print('not found')