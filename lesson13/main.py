'''
with open("group.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    line_count = 0
    for row in csv_reader:
        print(row)



with open("group.txt") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ",")
    for row in csv_reader:
        print(row)



a = []
b = {1:2}
with open("group.txt") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ",")
    for row in csv_reader:
        a.append(row)
        b.update(row)
        print(row)
print(a)
print(b)



with open("group_2.csv", mode="w") as csv_file:
    group_wrigter = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    group_wrigter.writerow(["name", "group", "birthday"])
    group_wrigter.writerow(["Maria", "python", "March"])
    group_wrigter.writerow(["Olexii", "python", "November"])


with open("group_2.csv", mode="w") as csv_file:
    field_names = ["name", "group", "birthday"]
    group_wrigter = csv.writer(csv_file, fieldnames = field_names)
    group_wrigter.writeheader()
    group_wrigter.writerow(['name':'Olexii', 'group':'python', 'birthday':'November'])


#example 2
new_list = []
with open('group_2.csv', 'r') as examp:
    reader_csv = csv.reader(examp, delimiter=',')
    for row in reader_csv:
        new_list.append(row)

print(new_list)

new_list.append(['Olexii_3', 'python_3', 'November_3'])

print(new_list)

with open('group_3.csv', 'w', newline='') as examp_2:
    writer_csv = csv.writer(examp_2, delimiter= ',')
    #writer_csv.writerows(new_list)
    for row in new_list:
        writer_csv.writerow(row)


a = [1, 2, 3]
for el in a:
    print(el)



numbers = [1, 2, 4, 7, 5]
numbers_iterator = iter(numbers)
print(numbers_iterator)
for number in numbers_iterator:
    print(number)
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))


a = []
def my_gen():
    counter = 0
    while True:
        yield counter **2
        counter +=1
generator = my_gen()
a.append(next(generator))
a.append(next(generator))
a.append(next(generator))
print(a)


a = []
def my_gen():
    counter = 0
    while counter<100:
        yield counter **2
        counter +=1
    yield "we are finished"
generator = my_gen()
for item in generator:
    print(item)



a = []
def my_gen():
    counter = 0
    while counter<100:
        yield counter **2
        counter +=1
    yield "we are finished"
generator = my_gen()
print(next(generator))
print(next(generator))
print(next(generator))
'''
