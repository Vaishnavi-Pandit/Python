# to count no of objects for a class.
class Sample:
    x=0 #this is class variable or static variable.
    def __init__(self):
        Sample.x+=1
    @staticmethod #decorator
    def display():
        print('no of objects created: ',Sample.x)

s1= Sample()
s1.display()
s2= Sample()
s3= Sample()
Sample.display()