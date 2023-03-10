def fizz_buzz(n):
    for x in range(1, n+1):
        s = x % 3
        a = x % 5
        if (s == 0 and a == 0):
            print("FizzBuzz")
        elif (a == 0):
            print("Buzz")
        elif (s == 0):
            print("Fizz")
        else:
            print(x)
fizz_buzz(18)