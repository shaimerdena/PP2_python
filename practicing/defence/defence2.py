def generating(n):
    value = n
    while value > 0:
        yield value 
        value -= 1
    
for i in generating(5):
    print(i, end = " ")
print()

import datetime

today = datetime.datetime.today()
print((today+datetime.timedelta(days=5)).strftime("%d"))
print((today-datetime.timedelta(days=5)).strftime("%d"))