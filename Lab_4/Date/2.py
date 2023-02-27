import datetime
from datetime import date, timedelta



print("Yesterday", date.today() - timedelta(1),(datetime.datetime.now()- timedelta(1)).strftime("%A"))
print("Today", date.today(),(datetime.datetime.now()).strftime("%A"))
print("Tomorrow", date.today() + timedelta(1),(datetime.datetime.now() + timedelta(1)).strftime("%A"))