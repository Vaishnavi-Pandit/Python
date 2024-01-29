x=0
while x<10:
    x+=1
    if x==5:continue#lop will just stop at 5 but will run other elements.
    print(x)
    if x>8:
        continue#will only print upto 8 afterwards it will stop printing.
    print(x)
print('outside the loop')