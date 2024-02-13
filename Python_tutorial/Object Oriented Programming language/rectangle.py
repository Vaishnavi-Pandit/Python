#create a rectangle clas from square class and display their areas
from square import *
class Rectangle(Square):
    def setareaofrect(self,a,b):
        self.a=a
        self.b=b
        self.ar=self.a*self.b

    def getareaofrect(self):
        return self.ar
