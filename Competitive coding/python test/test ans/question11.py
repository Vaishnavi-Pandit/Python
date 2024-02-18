
str=input('enter a string: ')
st=[]
for i in range(0,len(str)):
    count=0
    for j in range(0,len(str)):
        if str[i]==str[j]:
            count=count+1
        j=j+1
    if str[i] in st:
        continue;
    else:
        print(str[i],count)
        st.append(str[i])
    i=i+1