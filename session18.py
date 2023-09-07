import turtle

display_surface = turtle.Screen()
sides = int(display_surface.textinput(
    "Draw shape", "How many Sides do you want?"))

COLORS = ("red", "green", "blue", "purple", "yellow")

i = int(display_surface.textinput("Choose color", "(red = 0)\n(green = 1)\n(blue = 2)\n(purple = 3)\n(yellow = 4)"))



turtle.color(COLORS[i])
turtle.pensize(4)
for i in range(sides):
    turtle.forward(150)
    turtle.left(360/sides)


turtle.done()
