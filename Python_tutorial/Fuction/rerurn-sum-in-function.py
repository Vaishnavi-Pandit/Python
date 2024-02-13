def sumndiff(a,b):
    c=a+b
    d=abs(a-b)#abs function is used to wright the absolute value.
    e=(a-b)
    return c,d,e
n=float(input())
m=float(input())
res1,res2,res3=sumndiff(n,m)
print(res1)
print(res2)
print(res3)
print(sumndiff(n,m))