import time
from datetime import datetime

t = time.localtime()
current_time = time.strftime("%H:%M %p", t)
print(current_time)


date_string = '21:56 PM'
format = '%H:%M %p'
my_date = datetime.strptime(date_string, format)
custom_time = my_date.strftime(format)
print( custom_time)

x = datetime.datetime.now()
print(x.strftime("%A")) # to print day 

while(True):
    if(custom_time == current_time):
        print("hello\n")
    else:
        print("No hello")
        break
