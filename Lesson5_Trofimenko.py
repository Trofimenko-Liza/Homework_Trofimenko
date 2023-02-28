
# task 1
set_1 = {0, 2, 3, 4, 4, 2, 5, 6, 1, 7}
set_2 = {7, 1, 4, 2, 5, 6, 1, 8,9}
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


# task 2
user = {
    1: "Ivan",
    2: "Maya",
    3: "Maxim"
}
comand = int(input("Enter user id (1, 2, 3): "))
print(f"Hello", {user.get(comand, "all")} )


# task 3
set_4 = {1, 2, 8, 3, 2, 1, 1, 0, 9, 2, 3, 3, 3, 3, 7, 5, 2, }
print(len(set_4))


# task 4
set_5 = {0, 0, 1, 2, 1, 2, 5, 0}
set_6 = {3, 4, 5, 6, 7, 8, 0, 9}
set_7 = set_5 & set_6
print(set_7)
for element in set_7:
    print(element)
for element in set_5:
    print(element)
for element in set_6:
    print(element)


# task 5