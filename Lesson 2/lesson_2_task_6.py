list = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# вывести меньше 30
# вывести делятся на 3 без остатка
for i in range(0, len(list)):
    if list[i] <30 and list[i] % 3 == 0:
        print(list[i])
    