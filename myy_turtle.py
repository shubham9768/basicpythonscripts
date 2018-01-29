

import turtle

my_turtle = turtle.Turtle()

def square(length):
    my_turtle.forward(length)
    my_turtle.left(90)
    my_turtle.forward(length)
    my_turtle.left(90)
    my_turtle.forward(length)
    my_turtle.left(90)
    my_turtle.forward(length)

for i in range(10):
    square(100)



