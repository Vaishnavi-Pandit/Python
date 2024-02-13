#functions are first class objects.
#we can assign a fun to a var
#we can pass a function to another function.
#we can write a function inside another function
#we can return a function from another function.
'''def square(x):
    y=x*x
    return y
res=square(5)
print(res)'''

def display(f):
    str=f()
    #fun = name of function.
    #fun()=calling function.
    print("hello"+str)

def fun():
    return 'krish'
display(fun)

def dis():
    def fu():
        return 'krish'
    return 'hello'+fun()
print(dis())
