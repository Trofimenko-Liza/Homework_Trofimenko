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
