import math
import random

minute = int(random.randint(0, 59))
print(minute)
if minute >= 0 and minute < 15:
    print("It is first quarter of an hour")
elif minute >= 15 and minute <= 30:
    print("It is second quarter of an hour")
elif minute >= 31 and minute <= 45:
    print("It is third quarter of an hour")
elif minute >=46 and minute < 60:
    print("It is fourth quarter of an hour")
