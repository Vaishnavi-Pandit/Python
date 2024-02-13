# to know the current date and time
import time
from datetime import datetime

dt = time.ctime()
print(dt)

dt2 = datetime.today()  # datetime is class in the datetime module
print(dt2)
dt3 = datetime.now()
print(dt3)
