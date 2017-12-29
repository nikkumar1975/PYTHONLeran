import sys
print(sys.argv)

import math
print(math.sin(90))
print(math.log(512,2))

import random
print(random.randrange(6))

#for statistics we need Python 3.6.2 |Anaconda, Inc.|
#/Users/nkashyap/anaconda3/bin/python
import statistics
data = [90, 80, 80, 50, 70]
mean=statistics.mean(data)
print("mean= ",mean)
med=statistics.median(data)
print("median=",med)
mod=statistics.mode(data)
print("mod=",mod)


from datetime import date
curr = date.today()
print(curr)
bday = date(1975, 2, 5)
age =  curr - bday
print("age=",age.days)

print("end of chap10")
