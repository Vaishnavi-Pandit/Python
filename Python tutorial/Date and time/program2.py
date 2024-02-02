# Duration
from datetime import *
dt = datetime(2014,2,2,9,0,10)
duration = timedelta(weeks=10,days=5,hours=5,minutes=30,seconds=30)
print("Future date= ",dt+duration)
print("past date= ",dt-duration)