import turtle as t
import random

t.colormode(255)
pen = t.Turtle('turtle')
pen.speed('fastest')
pen.hideturtle()
color_list = [(233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174),
              (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155),
              (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43)]

pen.penup()
pen.setheading(225)
pen.forward(300)
pen.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    pen.dot(20, random.choice(color_list))
    pen.forward(50)
    if dot_count % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)

screen = t.Screen()
screen.exitonclick()
