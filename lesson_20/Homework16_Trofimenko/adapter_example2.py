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


#converter = CSVConverter()
#converter.read_file('example.csv')

    def write_file(self, filename:str):
        with open(filename, 'w', newline='') as writer:
            json.dump(self.__lines, writer, indent=4)


converter = JsonConverter()
converter.read_file('example.json')
converter.write_file('convert.csv')



import json
import csv




def read_json(filename):
    return json.loads(open('example.json').read())

def write_csv(data, filename):
    with open(filename, 'w+') as outf:
        writer = csv.DictWriter(outf, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

write_csv(read_json('example.json'), 'output.csv')