class Empo:
    def __init__(self):
        self.id=1001
        self.name="vaish"
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def setid(self,id):
        self.id=id

    def setname(self,n):
        self.name=n


E1=Empo()
id=E1.getid()
print(id)
nn=E1.getname()
print(nn)
E1.setid(788)
E1.setname("akhil")
print(E1.getid())
print(E1.getname())
