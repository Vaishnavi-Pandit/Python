#arithmatic-use.py for using module.
#4 different ways of using modules.
import arithmatic
arithmatic.add(19,34)
import arithmatic as ar #ar is used to replaces arithmatic name as it is so longer u can use arithmatic as well instead of ar when you haven't given ar as a nickname/aliasname.
ar.add(10,15)
res=ar.sub(18,14)
print(res)
from arithmatic import * #star represents all functions.
add(67,89)
from arithmatic import sub, add #mention the specific function that u want from module just to optimize the code
add(1,4)
print(sub(9,8))