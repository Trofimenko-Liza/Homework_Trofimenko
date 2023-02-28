
comand = input("enter comand:")
list_note = []

while comand == "add":
        # add new note
        add = input("enter new note:")
        list_note.append(add)
        print(list_note)
        comand = input("enter comand:")

        if comand == "earliest":
        # sorted by earliest->latest and print list
                earliest = sorted(list_note)
                print(earliest)
                comand = input("enter comand:")

        if comand == "latest":
        # sorted by latest->earliest and print list
                latest = sorted(list_note, reverse = True)
                print(latest)
                comand = input("enter comand:")

        if comand == "longest":
        # sorted by lenght, longest->shortest
                longest = sorted(list_note, key=len, reverse=True)
                print(longest)
                comand = input("enter comand:")

        if comand == "shortest":
        # sorted by lenght, shortest->longest
                shortest = sorted(list_note, key=len)
                print(shortest)
                comand = input("enter comand:")

        if comand == "exit":
        # enter exit and break programm
                        exit = str
                        break

else:
# processing wrong comand
        print("Incorrect comand")
