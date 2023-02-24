import math
import random


# task 1
minute = int(random.randint(0, 59))
print(minute)
if minute >= 0 and minute < 15:
    print("It is first quarter of an hour")
elif minute >= 15 and minute < 30:
    print("It is second quarter of an hour")
elif minute >= 30 and minute < 45:
    print("It is third quarter of an hour")
elif minute >=45 and minute < 60:
    print("It is fourth quarter of an hour")


# task 2
#while True:
birth_month = int(input ("Enter your birthday month: "))
if birth_month == 1 or birth_month == 2 or birth_month == 12:
    print("За вікном падав сніг")
elif birth_month == 3 or birth_month == 4 or birth_month == 5:
    print("Все довкола розцвітало")
elif birth_month == 6 or birth_month == 7 or birth_month == 8:
    print("Діти насолоджувались літніми канікулами")
elif birth_month == 9 or birth_month == 10 or birth_month == 11:
    print("Все довкола загоралось яскравими фарбами")
else:
    print("Введено некорректні дані. Будь ласка, введіть номер місяця вашого народження")


# task 3
number = int(random.randrange(1000000))
print(number)
last_number = number % 10
sum_number = 0
while number > 0:
    digit = number % 10
    if digit != 0:
        sum_number += digit
    number = number // 10
if last_number % 2 == 0 and sum_number % 3 == 0:
    print("Обране число ділиться на 6")
else:
    print("Обране число не ділиться на 6")


# task 4
x = float(input("Enter x: "))
y = float(input("Enter y: "))
if x > 0 and y > 0:
    print("I coordinate quarter")
elif x == 0 and y == 0:
    print( "the point is at start coordinate ")
elif x == 0 or y == 0:
    print ( "the point lies on the coordinate axis ")
elif x < 0 and y > 0:
    print("II coordinate quarter")
elif x < 0 and y < 0:
    print("III coordinate quarter")
else:
    print("IV coordinate quarter")
