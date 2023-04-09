import csv


new_list1 = []
def open_file():
    with open("doc.csv", 'r') as csv_file:
        reader_csv = csv.reader(csv_file, delimiter=',')
        for row in reader_csv:
            new_list1.append(row)
open_file()
print(open_file)


def edit_file():
    with open("doc.csv", mode="w") as csv_file:
        csv_edit = csv.writer(csv_file, delimiter=",")
        pass
print(edit_file)

new_list1.append(['Alex, Shevchenko, 25, Java'])
new_list1.append(['Maya, Polih, 42, Accountant'])
print(new_list1)

with open("doc2.csv", 'w', newline="") as csv_file2:
    csv_edit = csv.writer(csv_file2, delimiter=',')
    csv_edit.writerows(new_list1)





# task 2
'''
def generator_1():
    number = 0
    while number<100001:
        yield number **2
        number +=1

generator = generator_1()
for item in generator:
    print(item)

'''