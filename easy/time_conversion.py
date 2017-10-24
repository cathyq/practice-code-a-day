# Convert 12-hour AM/PM into 24-hour format.

#!/bin/python

import sys


time = "10:19:35PM"
a = []
for i in time:
    a.append(i)

hour = int("".join(a[:2]))
if hour == 12 and a[-2] == "A":
    hour = 0
elif hour == 12 and a[-2] == "P":
    hour = 12
elif a[-2] == "P":    
    hour = hour + 12   

hour = "%02d" % hour
minute = "".join(a[3:5])
sec = "".join(a[6:8])


print hour + ":" + minute + ":" + sec