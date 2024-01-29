#Duck Typing: Executing method without knowing its type.

class Duck:
    def talk(self):
        print('Quack quack!')
    def talk(self):
        print('Bow bow!')
def call_talk(obj):
    obj.talk() #without knowing type calling method.(duck typing)
d=Duck()
call_talk(d)
t=Dog()
call_talk(t)