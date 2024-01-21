'''g=25

def display():
    x=10
    print(g)
    print(x)


display()
print(g)'''
'''x=25

def display():
    x=10
    print(x)#local variables dominate global variables inside function locally.


display()
print(x)'''

x=25

def display():
    x=10
    print(x)#local variables dominate global variables inside function locally.
    y=globals()['x']#to acces global variables over local variables.
    print(y)

display()
print(x)