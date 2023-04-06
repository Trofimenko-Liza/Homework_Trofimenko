






# task 2
def generator_1():
    number = 0
    while number<100001:
        yield number **2
        number +=1

generator = generator_1()
for item in generator:
    print(item)