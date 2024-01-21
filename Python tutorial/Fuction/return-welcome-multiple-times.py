#write function that displays string multiple times
def pr(n,str):
    for i in range(1,n+1):
        print(str)
n=int(input('enter a no: '))
str=(input('enter a string : '))
pr(n,str)