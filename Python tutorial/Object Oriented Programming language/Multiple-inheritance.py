class Father:
    def height(self):
        print('Height= 6.0f')

class Mother:
    def color(self):
        print('color= tan')

class Child(Father,Mother):
    pass

ch=Child()
print("child's qualities:")
ch.height()
ch.color()