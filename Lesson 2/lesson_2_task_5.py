def month_to_season(a):
    if (a<=2) or (a == 12):
        print("Зима")
    elif (3<=a<=5):
        print("Весна")
    elif (6<=a<=8):
        print("Лето")
    else:
        print("Осень")
month_to_season(12)

""" 1 2= Зима
3 4 5 = Весна
6 7 8 = Лето
9 10 11 = Осень
12 = Зима """