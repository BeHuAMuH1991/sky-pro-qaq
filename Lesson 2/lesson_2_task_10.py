def bank(x, y):
    for i in range(1, y+1):
        x = x / 10 + x
    print(x)

bank(1000, 10)
