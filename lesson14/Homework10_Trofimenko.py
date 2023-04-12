import random







# task 2
item_count = {}
new_gen = [random.randint(1,10) for item in range(100)]
print(new_gen)
for i in new_gen:
    item_count[i] = new_gen.count(i)
    print(item_count)

