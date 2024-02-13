'''Create the student class with rno,name,marks in 5 subject.None
display the total marks and percentage of marks.'''
# rn, n, m are instance variable
# tm is the instance method.

class Student:
    def __init__(self, rn, n, m):
        self.roll = rn
        self.cl = n
        self.mar = m

    def tm(self):
        print("roll no: %d " %self.roll)
        print("class: %d" %self.cl)
        s = 0
        for i in self.mar:
            s = s + i
        print("sun= %d" %s)
        avg = s/len(self.mar)
        print("avg: %f" %avg)


P1 = Student(4, 5, [56, 78, 90, 45])
P1.tm()