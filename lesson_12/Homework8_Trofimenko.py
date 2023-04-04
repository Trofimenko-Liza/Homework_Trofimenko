import datetime



# task 2
def sum(a, b):
    try:
        return(o * b)
    except NameError as e:
       print("not supported type")
sum(1, 2)


# task 3
def changed_time():
    start = datetime.datetime(year=2022, month=2, day=24)
    difference = datetime.timedelta(days=-404)
    return(start - difference)
changed_time()
print(changed_time())

# task 4
def years_old():
    birth_time = datetime.datetime(year=2011, month=1, day=30)
    today = datetime.datetime.now()
    return(today - birth_time)
years_old()
print(years_old())


