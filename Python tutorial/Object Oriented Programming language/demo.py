# class and object examples.
class Person:
    # properties = vars
    # self is used to store meta-data so __init__ function is used.
    def __init__(self):
        self.name = 'Shrinu'
        self.age = 22

    # talk is method.
    def talk(self):
        print("hello i am %s" % self.name)
        print("my age is %d" % self.age)


# create object:
p1 = Person()
p1.talk()
print(p1) # will print the memory address.
