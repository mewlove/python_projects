# (control + '/' for comments)

import datetime

mytime = datetime.time(2,20,1,30)
print("Time:")
print(mytime)
print(mytime.hour)
print(mytime.min)

today = datetime.date.today()
print(f"Today: {today}")

from datetime import datetime
mydatetime = datetime(2021,10,3,14,20,1)
print(f"my datetime: {mydatetime}")

from datetime import date 
date1 = date(2021,6,6)
date2 = date(2021,6,8)
print(date2 - date1)