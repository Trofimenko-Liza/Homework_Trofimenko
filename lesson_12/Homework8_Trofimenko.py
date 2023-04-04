import datetime

# task 2
def sum(a, b):
    try:
        return(o * b)
    except NameError as e:
       print("not supported type")
sum(1, 2)


# task 3
time1 = datetime.datetime(year=2022, month=2, day=24)
time2 = datetime.timedelta(days=-100)
time3 = time1 - time2
print(time3)


