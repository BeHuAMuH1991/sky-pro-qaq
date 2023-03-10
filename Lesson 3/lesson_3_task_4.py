from turtle import *

my_turtle = Turtle()
my_turtle.speed(1)
my_turtle.screen.setup(1200, 800)

my_turtle.circle(100)
my_turtle.up()
my_turtle.goto(40,110)
my_turtle.down()
my_turtle.circle(10)
my_turtle.up()
my_turtle.goto(-40,110)
my_turtle.down()
my_turtle.circle(10)
my_turtle.up()
my_turtle.goto(0,60)
my_turtle.down()
my_turtle.circle(15)
my_turtle.up()
my_turtle.goto(5,73)
my_turtle.down()
my_turtle.circle(3)
my_turtle.up()
my_turtle.goto(-5,73)
my_turtle.down()
my_turtle.circle(3)
my_turtle.up()
my_turtle.goto(-20,30)
my_turtle.down()
my_turtle.circle(100,30)
my_turtle.ht()

""" # нарисовать квадрат
def draw_rect(t):
    for x in range(0, 4):
        t.right(90)
        t.forward(100)

 # рисует квадраты в цикле
for x in range(0, 360):
    draw_rect(my_turtle)
    my_turtle.right(1) """

# необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop() 
