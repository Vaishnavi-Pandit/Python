p=input("Enter a string")
y=p.strip()
lst=[1,0,2,3,4,5,6,7,8,9]
for i in y:
    if all i in lst:
        continue
    else:
        print('Not all integers')

