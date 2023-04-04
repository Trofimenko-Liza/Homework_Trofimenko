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
def years_old2():
    birth_time = datetime.datetime(year=2011, month=1, day=30)
    today = datetime.datetime.now()
    return(datetime.datetime.timestamp(today) - datetime.datetime.timestamp(birth_time))
years_old2()
print(years_old2()/31536000)  # разделила на кол-во секунд в году и получила кол-во лет


