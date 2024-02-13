# to accept a date and display the day of the week.
from datetime import *
d, m, y = [int(i) for i in input('Enter a date(dd/mm/yyyy): ').split('/')]
dt = date(y, m, d) # dateclass object
st = dt.strftime("you are born on %A and it is %jth day")
print(st)
