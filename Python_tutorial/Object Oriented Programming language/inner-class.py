# inner class demo
class Student:
    def __init__(self):
        self.rno = 90
        self.name = "vaish"

    def display(self):
        print("roll no= ", self.rno)
        print("name= ", self.name)

    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 9
            self.yy = 2001

        def display(self):
            print("Date of birth= {}/{}/{}".format(self.dd, self.mm, self.yy))


# multiple ways to access inner class and its method.
p1 = Student()
p1.display()
d = p1.Dob()
d.display()
t = Student().Dob()
t.display()
Student().Dob().display()

