# to sort a group of dates

from datetime import *

n = int(input('hoe many dates?: '))
lst = []
for i in range(n):
    d, m, y = [int(x) for x in input('Enter date(dd/mm/yyyy): ').split('/')]
    dt = date(y, m, d)
    lst.append(dt)
lst.sort()
print("sorted dates: ")
for i in lst:
    print(i)
