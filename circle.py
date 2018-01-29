

import turtle

my_turtle = turtle.Turtle()

my_turtle.speed(0)

def square(length,angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

for i in range(100):
    square(100,90)
    my_turtle.right(11)


#circle has 360 degree so 360/10 = 36 it will not repeat after 36 proper squares.
