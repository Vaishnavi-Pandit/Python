#to display squares of integer from 1 to 10
#original code without list comphrension
lst=[]
for i in range(1,11):
    lst.append(i*i)
print(lst)
#code with list comphrension
list=[i*i for i in range(1,11)]
print(list)