#a eregex to search for string starting with m and having total three characters.
import re
s= "hello\nworld!"
print (s)
t=r"hello\nworld!"#after using r the \n is treated as string
print(t)
str="Man sun mop rat cat rot tom maf msd mkg"
ob=re.search(r'm\w\w',str)# r is raw string \w means any alphanumeric characters.
lst=re.findall(r'm\w\w',str)# r is raw string \w means any alphanumeric characters.
print(lst)
if ob:
    print(ob.group())
else:
    print("not found")
obj=re.match(r'm\w\w',str)
if obj:
    print(obj.group())
else:
    print("not found")