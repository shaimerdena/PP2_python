# Write a Python program to drop microseconds from datetime.

import datetime

today = datetime.datetime.today()
without_microseconds = today.replace(microsecond=0)

print(without_microseconds)