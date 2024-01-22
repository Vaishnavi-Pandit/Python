# generator function to display nos from m to n
#generator function will never display result it will store the result in object that's why instead of print it uses yield function
def gen(m,n):
    while m<=n:
        yield m
        m=m+1
v=gen(10,20)
#print(list(v))
for i in v:
    print(i)