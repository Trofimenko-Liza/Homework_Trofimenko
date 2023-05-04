# task 1

import json
import csv

class JsonConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename:str):
        with open(filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.__lines.append(line)
            print(self.__lines)

    def write_file(self, filename:str):
        with open(filename, 'w', newline='') as writer:
            json.dump(self.__lines, writer, indent=4)


converter = JsonConverter()
converter.read_file('example.json')
converter.write_file('convert.csv')


new_list = []
def open_file():
    with open("convert.csv", 'r') as csv_file:
        reader_csv = csv.reader(csv_file, delimiter=',')
        for row in reader_csv:
            new_list.append(row)
open_file()


def edit_file():
    with open("convert.csv", mode="w") as csv_file:
        csv_edit = csv.writer(csv_file, delimiter=",")
        pass

new_list.append(['Alex', 'Shevchenko', 25, 'Java'])

with open("convert.csv", 'w', newline="") as csv_file2:
    csv_edit = csv.writer(csv_file2, delimiter=',')
    csv_edit.writerows(new_list)
