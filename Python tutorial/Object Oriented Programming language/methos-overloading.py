#method overloading: same method performing different tasks.
class Myclass:
    @staticmethod
    def add_all(*x):
        res=sum(x)
        return res
r1=Myclass.add_all(10,11)#sum of 2 nos
print(r1)
r2=Myclass.add_all(9,5,6,78)#sum of 4 nos
print(r2)
#same method add_all is adding 2 as well as 4 elements means performing two tasks or actions that's why method overloading.