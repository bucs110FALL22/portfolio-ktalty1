lsimport turtle
#Using Loops to make code shorter!!
CIRCLE_DEG = 360
window = turtle.Screen()

sides = 4
length = 50
colors = ["red", "purple", "green"]
for c in colors:
  my_turtle.color(c)
  for i in [0]*sides:
    my_turtle.left(CIRCLE_DEG / sides)
    my_turtle.forward(length)


my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
sides = 4
length = 50
my_turtle.color("purple")
my_turtle.forward(length)
my_turtle.left(360 / sides)
my_turtle.forward(length)
my_turtle.left(360 / sides)
my_turtle.forward(length)
my_turtle.left(360 / sides)
my_turtle.forward(length)
my_turtle.left(360 / sides)

my_turtle.up()
my_turtle.forward(100)
my_turtle.down()

my_turtle.color("red")
my_turtle.forward(length)
my_turtle.left(CIRCLE_DEG / sides)
my_turtle.forward(length)
my_turtle.left(CIRCLE_DEG / sides)
my_turtle.forward(length)
my_turtle.left(CIRCLE_DEG / sides)
my_turtle.forward(length)
my_turtle.left(CIRCLE_DEG / sides)

window.exitonclick()