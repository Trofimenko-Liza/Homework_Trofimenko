# task 1

from lesson_11.arithmetics import  sum
from lesson_11.folder2.arithmetics2 import difference
from lesson_11.folder2.folder3.arithmetics3 import multi
from lesson_11.folder2.folder3.arithmetics3 import devide
from lesson_12.arithmetics4 import percent

Lina_salary = 1100
Kirill_salary = 1000

print(sum(Lina_salary, Kirill_salary))
print(difference(Lina_salary, Kirill_salary))
print(multi(Lina_salary, Kirill_salary))
print(devide(Lina_salary, Kirill_salary))
print(percent(Lina_salary, Kirill_salary))



# task 2
def sum(a, b):
    try:
        return(o * b)
    except NameError as e:
       print("not supported type")
sum(1, 2)



import datetime
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


