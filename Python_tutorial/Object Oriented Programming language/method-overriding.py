#Method overraiding means Writing same method in subclass as that of super class.
class Super:
    def Dispay(self):
        print('super class method')

class Sub(Super):
    def Display(self):
        print('sub class method')

s=Sub()
s.Display()#sub class method is overiding the super class method.