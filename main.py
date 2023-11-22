from turtle import Turtle, Screen, colormode
import random

colormode(255)
timmy = Turtle()
timmy.speed(0)


def random_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color_gen())
        timmy.circle(100)
        timmy.seth(timmy.heading() + 10)


draw_spirograph(36)
# angles = [0, 90, 180, 270]
#
# for side in range(200):
#     timmy.color(random_color_gen())
#     deg = random.choice(angles)
#     timmy.fd(30)
#     timmy.seth(deg)































screen = Screen()
screen.exitonclick()
