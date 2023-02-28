
comand = input("enter comand:")
list_note = []

while comand == "add":
        add = input("enter new note:")
        list_note.append(add)
        print(list_note)
        comand = input("enter comand:")

        if comand == "earliest":
                earliest = sorted(list_note)
                print(earliest)
                comand = input("enter comand:")

        if comand == "latest":
                latest = sorted(list_note, reverse = True)
                print(latest)
                comand = input("enter comand:")

        if comand == "longest":
                longest = sorted(list_note, key=len, reverse=True)
                print(longest)
                comand = input("enter comand:")

        if comand == "shortest":
                shortest = sorted(list_note, key=len)
                print(shortest)
                comand = input("enter comand:")

        if comand == "exit":
                        exit = str
                        break

else:
        print("Incorrect comand")
