class Bank:
    def __init__(self):
        self.account=1001
        self.name="vaish"
        self.add="balaji nagar"
        self.phone=658686999
        self.bal=456989
        self.__loan=87579
    def display_to_clerk(self):
        print("Account no = ",self.account)
        print("Name= ",self.name)
        print("address= ",self.add)
        print("phone no= ",self.phone)
        print("balance= ",self.bal)

    def display_to_accountant(self):
        print("Account no = ", self.account)
        print("Name= ", self.name)
        print("address= ", self.add)
        print("phone no= ", self.phone)
        print("loan= ", self.__loan)

d = Bank()
d.display_to_clerk()
d.display_to_accountant()
'''print(d.loan)#anyone can manupilate data in encapsulation. so '__loan' is used'''
print(d._Bank__loan)#name mangling