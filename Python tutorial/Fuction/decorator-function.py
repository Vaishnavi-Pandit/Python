# decorate function to increment the result of another function
def decor(fun):
    def inner():
        res=fun()
        res=res+100
        return res
    return inner()
def myfun():
    return 10
f=decor(myfun)
n=f()
print(n)