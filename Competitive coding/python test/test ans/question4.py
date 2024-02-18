t=input('Enter a string: ')
count=0
lst=['a','i','o','e','u']
for i in t:
    if i in lst:
        count=count+1

print('There are %d vowels.'%count)
