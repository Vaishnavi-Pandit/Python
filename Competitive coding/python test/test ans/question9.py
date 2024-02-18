lst=input('Enter a string: ')
lst1=[]
for i in range(0,len(lst)):
    if lst[i]=='0' or lst[i]=='1' or lst[i]=='2' or lst[i]=='3' or lst[i]=='4' or lst[i]=='5' or lst[i]=='6' or lst[i]=='7' or lst[i]=='8' or lst[i]=='9':
        lst1.append(lst[i])
print(lst1)

