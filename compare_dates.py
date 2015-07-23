#!/usr/bin/python
import time
with open("/home/mwidjaja/dates.txt") as f:
    contents = f.readlines()

for i in contents:
    date1, date2 = i.split(',')
    date1 = date1.strip('"')
    date2 = date2.split('T')[0].strip('"') 
    date1a = time.strftime("%Y-%m-%d",time.strptime(date1, "%m/%d/%Y"))
    print i if date1a == date2 else None
  
