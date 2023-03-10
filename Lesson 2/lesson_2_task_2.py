
def is_year_leap(a):
    if (a % 4 == 0):
        print("Год", a, "высокостный")
    else:
        print("Год", a, "не высокостный")
    
is_year_leap(2224)