import csv
'''
new_list1 = []
def open_file():
    with open("doc.csv") as csv_file:
        return(new_list1)
open_file()

new_list2 = []
def edit_file():
    with open("doc2.csv", mode="w") as csv_file:
        pass
edit_file()
'''


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






