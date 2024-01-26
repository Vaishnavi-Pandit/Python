# class and object examples.
class Person:
    # properties = vars
    # self is used to store meta-data so __init__ function is used.
    def __init__(self,n,a):
        self.name = n
        self.age = a

    # talk is method.
    def talk(self):
        print("hello i am %s" % self.name)
        print("my age is %d" % self.age)


# create object:
p1 = Person('shiksha',23)
p2=Person('sita',45)
p2.talk()
p1.talk()
print(p1) # will print the memory address.