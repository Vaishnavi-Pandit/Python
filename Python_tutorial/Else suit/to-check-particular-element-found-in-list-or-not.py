#to check if a particular element is found in the list or not
lst=[40,60,69,56,67]
n=int(input('Which element to find: '))

for i in lst:
    if i==n:
        print('yes')
        break
else:
    print("not found")         

if n in lst:print ('found')
else:print("not found")