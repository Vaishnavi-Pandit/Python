#positional arguments
def join(s1,s2):
    str =s1+s2
    return str

a="Auranga"
b="bad"
e=join(a,b)#positional arguments.
print(e)
f=join(s1=b, s2=a)#keyword arguments
print(f)

#default arguments
def gr(item, price=50.00):
    print('item name= ',item)
    print('price= Rs.%.2f'%price)
gr('oil')
gr('sugar',65)

#Variable length argument
#here x is variable length basically it is in tuple form
#variable length argument should be last in all arguments in the function.
def total(num, *x):
    tot=num+sum(x)
    print("total=",tot)
total(100,10)
total(100,30,40,60,70)

