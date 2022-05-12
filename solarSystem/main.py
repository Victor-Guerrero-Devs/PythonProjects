import turtle
from random import randint, random

pen = turtle.Turtle()


def jump_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def get_orbit(x, y):
    from math import hypot
    return hypot(x, y)


def draw_planet(x, y, size, color, name):
    pen.speed(10)
    orbit_size = get_orbit(x, y)
    jump_to(0, -orbit_size)
    pen.circle(orbit_size)

    jump_to(x, y - size)

    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

    jump_to(x, y + size)

    pen.write(name, align="center", font=("courier", 18, "bold"))


draw_planet(0, 0, 20, "yellow", "Sun")
draw_planet(0, 55, 10, "dark red", "Mercury")
draw_planet(-50, -60, 18, "orange", "Venus")
draw_planet(120, 20, 20, "light blue", "Earth")
draw_planet(0, -160, 15, "red", "Mars")
draw_planet(-220, 150, 30, "brown", "Jupiter")
draw_planet(190, -230, 28, "goldenrod", "Saturn")
draw_planet(-330, 40, 26, "powder blue", "Uranus")
draw_planet(400, 20, 25, "royal blue", "Neptune")


def randomize_turtle():
    size = random() * 0.5 + 0.5
    pen.shapesize(size)

    grey = random()
    pen.color(grey, grey, grey)


radius = 210
pen.speed(10)
pen.shape("circle")
jump_to(0, -radius)
offset = 10
pen.penup()
for i in range(100):
    x_start, y_start = pen.pos()

    x_offset = randint(-offset, offset)
    y_offset = randint(-offset, offset)
    randomize_turtle()
    pen.goto(x_start + x_offset, y_start + y_offset)
    pen.stamp()

    pen.goto(x_start, y_start)
    pen.circle(radius, 3.6)


pen.getscreen().exitonclick()