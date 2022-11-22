
from datetime import datetime, date

t1 = date(year = 2001, month = 2, day = 28)
t2 = date(year = 2000, month = 2, day = 28)
t3 = t1 - t2
print('There are', t3, 'days between', t1, 'and', t2)