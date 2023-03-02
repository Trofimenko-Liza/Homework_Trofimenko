
# task 1
set_1 = {0, 7,  2, 3, 4, 4, 2, 5, 6, 1, 7}
set_2 = {7, 9, 1, 4, 2, 5, 6, 1, 8,9}
set_3 = set_1 & set_2
print(set_1.intersection(set_2) )


#task 2
students_score = {
    "Matvii": 20,
    "Makar": 25,
    "Aia": 10,
    "Semen": 15
    }

avarage = sum(students_score.values()) / len(students_score)

for student in students_score.keys():
        if students_score[student] > avarage:
            print(student)


# task 3
set_4 = {1, 2, 8, 3, 2, 1, 1, 0, 9, 2, 3, 3, 3, 3, 7, 5, 2, }
print(len(set_4))


# task 4
set_5 = {0, 0, 1, 2, 1, 2, 5, 0}
set_6 = {0, 3, 4, 9, 9, 5, 6, 7, 8, 0, 9}
set_7 = set_5 & set_6
for element in set_7:
    print(element)
for element in set_5:
    print(element)
for element in set_6:
    print(element)


# task 5
set_8 = ['one', 'two', 'three', 'one', 'four', 'five', 'seven', 'ten', 'seven', 'one']
count_one = set_8.count('one')
count_two = set_8.count('two')
count_three = set_8.count('three')
count_four = set_8.count('four')
count_five = set_8.count('five')
count_seven = set_8.count('seven')
count_ten = set_8.count('ten')
print(("one", + count_one), ("two", + count_two), ("three", + count_three), ("four", + count_four),
("five", + count_five),("seven", + count_seven), ("ten", + count_ten))