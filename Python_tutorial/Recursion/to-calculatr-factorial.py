def fact(n):
    if n==0:
        return 1
    else:
        v=n*fact(n-1)
        return v
        
y=int(input('Enter a no: '))
print(fact(y))