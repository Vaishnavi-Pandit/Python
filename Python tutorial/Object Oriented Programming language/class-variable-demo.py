#class variable demo
class Myclass:
    x=10 #this is class variable.
    @classmethod #decorator
    # cls stores the memory of class namespace.
    # self stores the memory of objects in that class.
    def modify(cls):
        cls.x+=1 # increment class variable by 1.

m1= Myclass()
m2= Myclass()
print(m1.x,m2.x)
m1.modify() #classname.modify()
print(m1.x,m2.x)#because same copy is available in both m1 and m2 thats why modification done in m1 will be displayed in m2 as well.

m1.x+=1
print(m1.x,m2.x)#here i made changes outside the method that's why changes made in m1 will not affect m2