
# task 1
def summa(func):
    def inner():
        print('This is summa')
        func()
        print(func())

    return inner


def multy(func):
    def inner():
        print('This is multy')
        func()
        print(func())

    return inner


@summa
def calculate_sum(a=3, b=6):
    return a + b

calculate_sum()

@multy
def calculate_multy(a=5, b=7):
    return a * b

calculate_multy()






# task 2

import random

item_count = {}
new_gen = [random.randint(1,10) for item in range(100)]
print(new_gen)
for i in new_gen:
    item_count[i] = new_gen.count(i)
    print(item_count)



